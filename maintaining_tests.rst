PLUGINS
=======
In order to use a ``pytest`` plugin, one will have the install it first using ``pip install pytest-xxx``, like ``pip install pytest-cov`` for the coverage plugin for ``pytest``. 

pytest-cov
----------
- By using the ``pytest-cov`` plugin, one can check which lines in a package or set of scripts are currently covered by all pytests;
- Instead of executing ``pytest``, executing ``pytest --cov --cov-report=term-missing`` will automatically track coverage over all pytests and print out the results later;
- Optionally, one could add the ``--cov-branch`` option to also get a report on branch coverage (which was explained by Will);
- It is also possible to write these options into a ``setup.cfg`` file, such that they are automatically used whenever ``pytest`` is executed;
- In the same file, one can also write options for the ``pytest-cov`` plugin itself (or ``coverage.py``, as that is what the package is actually called that runs it in the background);

pytest-pep8
-----------
- Pytest can also automatically test every file for PEP8-compliance with the ``pytest-pep8`` plugin;
- This can be enabled by adding the ``--pep8`` option to pytest, or by adding it to the ``setup.cfg`` file;
- With this plugin enabled, ``pytest`` will automatically fail any file that is not PEP8-compliant (which therefore fails the entire test run as well);
- Currently, the scripts in this repo are not PEP8-compliant, as you will see when adding the ``--pep8`` option;


Continuous Integration (CI)
===========================
Another important part of maintaining your code/tests, is by using a continuous integration (CI) service, like Travis CI (https://travis-ci.com).
A CI service allows you to execute a series of specified tests on the GitHub repo, every time a commit (or set of commits) is being pushed.
However, unlike executing tests on your own computer, a CI service can do this using far more flexibility and this can be integrated into your GitHub repo.
**Should ``tox`` be mentioned here?**

What is a CI service?
---------------------
So, what does a CI service like Travis CI do exactly?
Once set up properly for your GitHub repo, Travis will be notified by GitHub every time a push has been made.
When a push was made, Travis will automatically set up a collection of environments (as specified by the ``.travis.yml`` file), clone the repo and execute a bunch of scripts.
These scripts can range from simply installing all the requirements and doing the pytests; to checking if a repo can be packaged up properly; to even generating and uploading entire webpages.
It allows for many pipelines to be automated.
Here, we just focus on getting our pytests done, which requires the simple ``.travis.yml`` file in this repo.

One thing to remember when using a CI service, is that it starts off completely blank.
This means that you have to specify everything that is required to execute the tests.
The benefit of this is that it makes it really easy to spot if you forgot to add a requirement somewhere (as a test will crash or fail), or made an assumption about the state of the system (for example, Windows uses 32-bit and 64-bit versions of its OS, while Linux and Mac OS-X solely use 64-bit versions).
It also allows you to check your code using OSs or Python versions that you do not have access to (especially in the case of the former).

Another cool thing about using a CI service, is that they can report their status back to GitHub on the specific commit they used.
This, for example, allows for a CI service to FAIL a commit if one of their tests failed, informing you immediately that there is something wrong with that commit.
It is generally speaking a good idea to have at least one CI service active for your GitHub repo at all times, especially if it is something that will be open-source.
Travis CI is one of the few CI services that allows for private repos to be tested as well for no cost, although with a reduced capacity.


Coverage
========
Why do coverage?
----------------
Coverage in your code is very important for many different things, with the most important ones being:

- It allows you to write near-exhaustive tests for your scripts: You can track what parts of your code require special tests to be triggered;
- It checks for redundancy in your code: If you cannot find a single way to make a part of your code execute (as it covers a case that was already covered earlier for example), then that code is probably redundant or unnecessary (this happens much more than you think);
- It also can inform you very quickly when newly added features are currently not tested for, as your code coverage will have decreased;
- At the same time, as you usually write special case tests to cover exception cases in your code (got to get that coverage up), adding new features will automatically check if everything is still compatible;

Generally speaking, it is a good idea to always aim for 100% coverage.
If you cannot reach 100% coverage, ask yourself why this is:

- Is it impossible to ever execute this specific code block?
- Can this code block only be executed in very special exception cases that cannot be recreated under normal circumstances (like, catching memory overflows)?
- Is this code block operating system or architecture-specific (like, having a code block solely for Windows machines, but you are testing on Linux)?
- Or, analogously, is this code block Python version specific (Python 2 and 3)?

One way of dealing with some of these issues, is by using a CI service as introduced before.
If it is absolutely impossible to cover a code block under normal circumstances, but you are certain that this code block should be included, you can mark it as ''cannot be covered'' by adding ``# pragma: no cover`` to every line that cannot be covered, or to a code branch (like an if-statement).

Example Code
------------
Let's say you have the following code:

.. code:: python

    main_code()
    if flag:
        do_action()
        do_another_action()
    main_code_continued()

If in this code snippet, the if-statement cannot be executed under normal circumstances (and therefore cannot be covered), you can exclude it by writing it like this:

.. code:: python

    main_code()
    if flag:  # pragma: no cover
        do_action()
        do_another_action()
    main_code_continued()

This will automatically exclude the if-statement and everything inside it from the code coverage.


Example Coverage
----------------
An example of a coverage output using ``pytest`` would be:

.. code:: bash

    ----------- coverage: platform win32, python 3.6.6-final-0 -----------
    Name                             Stmts   Miss  Cover   Missing
    --------------------------------------------------------------
    example_scripts\__init__.py          0      0   100%
    example_scripts\downsampler.py      91     69    24%   39-103, 141-172, 215-217, 222-225, 228-231, 263-273
    example_scripts\galaxy.py           58     21    64%   51-52, 149, 168-169, 206-219, 245-254
    --------------------------------------------------------------
    TOTAL                              149     90    40%

This is the output of the current pytest coverage of this repo.
It tells us that there are still some lines left in the ``galaxy.py`` file to be covered, and many lines in the ``downsampler.py``.


CodeCov
-------
After running your tests on, let's say, Travis CI, it is also possible to upload the coverage report to CodeCov.
CodeCov is a coverage service, that automatically tracks the code coverage of a repo.
This allows you to combine all the coverage reports produced by the different jobs on Travis, and put them in a single place.
As with Travis CI, CodeCov will add a status report to the commit it is about.

Unlike Travis CI, CodeCov does not need a special .yml-file in order to function (although it does allow for more options).
The only thing that is necessary to do, is go to https://codecov.io, login with your GitHub account and activate the repo you want to do code coverage for.
After that, you can either manually sent the coverage reports, or you can add two lines to your ``.travis.yml`` file with::

    after_success:
    - codecov

If you make sure that you have the Python package ``codecov`` installed, then Travis will automatically send any made coverage reports to CodeCov.

Additionally, one can make a ``.codecov.yml`` file in the repo root directory (like the ``.travis.yml`` file).
Here, one can specify the different options that CodeCov needs to take into account, and how you want the code coverage to be reported on the repo.
Using this, it is also possible for CodeCov to FAIL a commit (like Travis CI can) if its coverage does not meet a specified threshold (currently, this is not done in the ``.codecov.yml`` file).
For example, you can make a commit fail if the code coverage of the entire package falls below 95%, or if the code coverage of the made changes is below 90% (and so on).
This can be extremely useful when you have an open-source package and others make pull requests to your package, while it also enforces you to keep all your tests up-to-date.

