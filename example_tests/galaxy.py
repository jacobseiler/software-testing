"""
In this module, we're generating a bunch of Galaxy objects and then doing some
calculations on them.

We've implemented some tests in ``test_galaxies.py``.

Implemented Tests
-----------------

Ensure that the class can be called!

Generate some data using a pre-determined seed and check the results match the expected output.

Your Tasks
----------

Generate some random galaxies and properties and write them both to file.  In the test proper, read in the galaxies, execute the same functions, then check if the results match the answer written to file. 

Generate a random set of galaxies and check their output. How do you handle random numbers
in testing scenarios?

What happens when there are zero galaxies in the region passed to
``mass_within_region()``? How should we handle this case? Is there a "correct" answer?

Extend the module to handle 3 spatial dimensions. How would you update the tests to
account for this? BE CAREFUL! At every step, we want to ensure that our tests are still
passing.

Author: Jacob Seiler
"""

import numpy as np


class Galaxy(object):
    """
    Class to hold data associate with a galaxy.
    """

    def __init__(self, x, y, mass):
        """
        Instantiates a galaxy at a given position and mass.

        Parameters
        ----------

        x, y, mass: float
            The spatial positions and mass of the galaxy. Units are arbitrary.
        """
        self.x = x
        self.y = y

        self.mass = mass

    def __repr__(self):
        """
        A ``Galaxy`` will be represented as "[<x>, <y>] mass: <mass>". Much more useful than
        <Galaxy object at BLAH-USELESS-MEMORY-ADDRESS>
        """

        string = f"[{self.x}, {self.y}] mass: {self.mass}"
        return string


def mass_within_region(gals, x_bound, y_bound):
    """
    Calculate the total mass and number of galaxies within a specified region.

    Parameters
    ----------

    gals: list of ``Galaxy`` class instances.
        Galaxies that we're calculating the mass for.

    x_bound, y_bound: [float, float]
        The minimum and maximum bounds that define the region we're averaging
        inside.

    Returns
    -------

    mass_in_region: float
        The total galaxy mass within the specified region.

    num_gals_in_region: int
        The number of galaxies within the specified region.
    """

    # Initialize our counters.
    mass_in_region = 0.0
    num_gals_in_region = 0
    region_bounds = [x_bound, y_bound]

    for gal in gals:

        gal_pos = [gal.x, gal.y]
        in_region = True

        # We're going to go through each dimension of the galaxy and ask if the position is
        # inside the region.
        for region_bound, dim_pos in zip(region_bounds, gal_pos):

            # Galaxy is outside the region. Flag it and move to the next galaxy.
            if dim_pos < region_bound[0] or dim_pos > region_bound[1]:
                in_region = False
                break

        # Galaxy was in the region, add it.
        if in_region:
            mass_in_region += gal.mass
            num_gals_in_region += 1

    return mass_in_region, num_gals_in_region


def generate_random_data(boxsize=100.0, mass_factor=1.0, N=1000, seed=None,
                         write_to_file=True, fname_out="./test_data.txt",):
    """
    Generates random Galaxy instances. Either writes the galaxies to file
    or returns them depending upon the value of ``write_to_file``.

    Parameters
    ----------

    boxsize: float
        Galaxies are generated with a random x/y position in the range [0, 1) times by
        ``boxsize``. Hence this sets the maximum position of a galaxy.

    mass_factor: float
        Galaxies are generated with a random mass in the range [0, 1) times by
        ``mass_factor``. Hence this sets the maximum mass of a galaxy.

    N: integer
        Number of galaxies to generate.

    seed: int
        Seed used to initialize the state of the random generator. If ``None``, will use
        the system clock as defined by ``numpy.random.seed()``.

    write_to_file: bool
        If set, writes the generated galaxies to a file specified by ``fname_out``.
        Otherwise, returns a list of the generated galaxies.

    fname_out: string
        File name where the galaxies are written to. Required if ``write_to_file`` is set.

    Returns
    ---------

    If ``write_to_file`` is specified:
        ``N`` galaxies with random x/y positions and mass saved to file ``fname_out``.
        The data format is three columns: x y Mass.

    If ``write_to_file`` is not specified:
        gals: a list of ``Galaxy`` instances with length ``N``.
            Galaxies with random x/y positions and mass.
    """

    if seed:
        np.random.seed(seed)
    else:
        np.random.seed()

    # Generate numbers between 0 and 1 then scale by the size of the box. We will generate
    # 2N numbers then slice it later.
    random_pos = np.random.uniform(size=2*N) * boxsize

    x = random_pos[0:N]
    y = random_pos[N:2*N]

    mass = np.random.uniform(size=N) * mass_factor

    # We're either returning a list of galaxies or writing the values to file.
    if write_to_file:
        write_galaxies(gals, fname_out, boxsize, mass_factor, seed)

        return None

    else:

        gals = []
        for (pos_x, pos_y, mass_val) in zip(x, y, mass):
            gal = Galaxy(pos_x, pos_y, mass_val)
            gals.append(gal)

        return gals


def write_galaxies(gals, fname_out, boxsize, mass_factor, seed=None):
    """
    Writes a list of galaxies to file.

    Parameters
    ----------

    gals: list of ``Galaxy`` class instances.
        Galaxies that we're calculating the mass for.

    fname_out: string
        File name where the galaxies are written to.

    boxsize: float
        Galaxies are generated with a random x/y position in the range [0, 1) times by
        ``boxsize``. Hence this sets the maximum position of a galaxy.

    mass_factor: float
        Galaxies are generated with a random mass in the range [0, 1) times by
        ``mass_factor``. Hence this sets the maximum mass of a galaxy.

    seed: int
        Seed used to initialize the state of the random generator. This may have been used
        to generate random data using :py:func:`~generate_random_data()`.

    Generates
    ---------

    Saves a file named ``fname_out`` with the x/y positions and mass saved. The data
    format is three columns: x y Mass. 
    """

    with open(fname_out, "w") as f_out:

        # Be good to our future-selves and write a header.
        f_out.write(f"# Box-Size {boxsize}\n")
        f_out.write(f"# Mass-factor {mass_factor}\n")
        f_out.write(f"# Random seed {seed}\n")
        f_out.write(f"# x\ty\tMass\n")

        for (pos_x, pos_y, mass_val) in zip(x, y, mass):

            f_out.write(f"{pos_x} {pos_y} {mass_val}\n")

        print(f"Successfully wrote to {fname_out}")

    return


def read_data(fname):
    """
    Reads x/y/mass values from a file and initializes as a list of Galaxy class instances.

    Parameters
    ----------

    fname: string
        Name of file being read

    Returns
    -------

    galaxies: list of ``Galaxy`` class instances
        Galaxy data read from the file.

    Notes
    -----

    Written to pair with ``generate_random_data()``.
    """

    # We had a header with "#".
    gal_data = np.loadtxt(fname, comments="#")

    gals = []
    for gal_vals in gal_data:
        gal = Galaxy(gal_vals[0], gal_vals[1], gal_vals[2])
        gals.append(gal)

    print(f"Read {len(gals)} galaxies from {fname}")

    return gals
