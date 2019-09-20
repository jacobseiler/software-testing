"""
Tests the methods and functions in the ``galaxy`` module.

Implemented Tests
-----------------

Ensure that the class can be called!

Generate some data using a pre-determined seed and check the results match the expected output.

Your Tasks
----------

Test the ``write_galaxies`` option for ``generate_random_data``. Read this data back in
and ensure that it is correct.  Should this data be kept on disk after the test? Should
the test delete it?

Generate some random galaxies and properties and write them both to file.
In the test proper, read in the galaxies, execute the same functions, then check if the
results match the answer written to file.

Generate a random set of galaxies and check their output. How do you handle random numbers
in testing scenarios?

What happens when there are zero galaxies in the region passed to
``mass_within_region()``? How should we handle this case? Is there a "correct" answer?

Extend the module to handle 3 spatial dimensions. How would you update the tests to
account for this? BE CAREFUL! At every step, we want to ensure that our tests are still
passing.

Author: Jacob Seiler
"""

from example_scripts import galaxy

import pytest


def test_gal_class():
    """
    In this test, we just want to ensure that the Galaxy class can be instantiated. Easiest
    test ever but still could be useful!
    """

    gal = galaxy.Galaxy(0.5, -21.5, -20)

    assert(gal.x == 0.5)
    assert(gal.y == -21.5)
    #assert(gal.z == 142.4)
    assert(gal.mass == -20)


@pytest.mark.parametrize(
        "x_bound, y_bound, expected_mass, expected_N, seed",
        [([0,50.0], [23.0, 28.0], 17.55854294814121, 29, 777)]
        )
def test_mass_in_region(x_bound, y_bound, expected_mass, expected_N, seed):
    """
    Check that if we generate galaxies using a specific random seed, then the statistics
    match the expected values.

    Can you extend the ``parameterize`` decorator to test a few other combinations?

    Can you implement a similar test that reads previously generated galaxies, calculates
    some statistics, then compares the answer to the "correct" answer?

    In some instances, we may WANT a test to fail to check certain conditions. In these
    instances, we want the individual test to fail, but for the overall pytest to pass.
    Search the ``pytest.mark.parametrize`` docs for the correct way to do this. Can you
    choose some parameters to get this scenario to work? When would this be useful?

    Parameters
    ----------

    x_bound, y_bound: [float, float]
        The minimum and maximum bounds that define the region we're summing/averaging
        inside.

    expected_mass: float
        The mass inside the region specified by
        (x_bound[0], y_bound[0]), (x_bound[1], y_bound[1]).

    expected_N : int
        The number of galaxies inside the region specified by
        (x_bound[0], y_bound[0]), (x_bound[1], y_bound[1]).

    seed: int
        Seed used to initialize the state of the random generator. If ``None``, will use
        the system clock as defined by ``numpy.random.seed()``.
    """

    import numpy as np

    # First generate some random galaxies.
    gals = galaxy.generate_random_data(seed=seed)

    # If the seed is 777, then we know what the output should be.
    if seed == 777:

        mass_in_region, N_in_region = galaxy.mass_within_region(gals, x_bound, y_bound)

        # Because 'mass_in_region' is a floating point, don't want to test pure equality.
        test_result = np.allclose(mass_in_region, expected_mass)
        assert(test_result)

        assert(N_in_region == expected_N)

    # Can you implement a solution to handle truly random galaxies?
    else:

        # Is this enough for a debug message...?
        print("Tests for testing seeds other than 777 not implemented.")
        assert False
