# Archetypes for what kinds of testing scripts we should do

* Random numbers.
* Reading in FITS files.
* Floating points  (allclose).
* Older versions don't work (use an `astropy` API call that works now but
  doesn't work using an older version). Solution is to specify in the
  requirements that you need a specific version. Could have a manual check?
* Newer versions don't work. (use an `astropy` API call that used to work but
  doesn't work now). (Or a bug in `numpy`).
* Pulling data from the internet (NED).
* If you're using a particular reference, how do you ensure that you're getting
  the correct version?
* Expected number of rows/columns change.
* Should be failing early.  Maybe have some code where it fails at the end but
  the problem is actually at the start.
* Extending some code to add new features.
* Maybe some functions that explicit say what they expect and have tests that
  check what happens if you give it different things. E.g., function asks for a
  `numpy` array and you give it a float, what happens?
