PLUGINS
=======
pytest-cov
----------
- By using the ``pytest-cov`` plugin, one can check which lines in a package or set of scripts are currently covered by all pytests;
- Instead of executing ``pytest``, executing ``pytest --cov --cov-report=term-missing`` will automatically track coverage over all pytests and print out the results later;
- It is also possible to write these options into a ``setup.cfg`` file, such that they are automatically used whenever ``pytest`` is executed;
- In the same file, one can also write options for the ``pytest-cov`` plugin itself (or ``coverage.py``, as the package is actually called that runs it in the background);

pytest-pep8
-----------
- Pytest can also automatically test every file for PEP8-compliance with the ``pytest-pep8`` plugin;
- This can be enabled by adding the ``--pep8`` option to pytest, or by adding it to the ``setup.cfg`` file;
- With this plugin enabled, ``pytest`` will automatically fail any file that is not PEP8-compliant (which therefore fails the entire test run as well);
- Currently, the scripts in this repo are not PEP8-compliant, as you will see when adding the ``--pep8`` option;


Coverage
========
Why do coverage?
----------------
Coverage in your code is very important for many different things, with the most important ones being:

- It allows you to write near-exhaustive tests for your scripts: You can track what parts of your code require special tests to be triggered;
- It checks for redundancy in your code: If you cannot find a single way to make a part of your code execute, then that code is probably redundant (this happens much more than you think);
- It also can inform you very quickly when newly added features are currently not tested for, as your code coverage will have decreased;
- At the same time, as you usually write special case tests to cover exception cases in your code (got to get that coverage up), adding new features will automatically check if everything is still compatible;

Generally speaking, it is a good idea to always aim for 100% coverage.
If you cannot reach 100% coverage, ask yourself why this is:

- Is it impossible to ever execute this specific code block?
- Can this code block only be executed in very special exception cases that cannot be recreated under normal circumstances (like, catching memory overflows)?
- Is this code block operating system or architecture-specific (like, having a code block solely for Windows machines, but you are testing on Linux)?
- Or, analogously, is this code block Python version specific (Python 2 and 3)?


One way of dealing with some of these issues, is by using a CI (continuous integration) service like Travis CI (https://travis-ci.com).
By using a CI service, one can perform all tests using all combinations of operating systems, architectures (sometimes at least) and Python versions.
If you are going to make your code publicly available (especially if it is going to be written up in a package), it is a really good idea to have at least one CI service active.

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

If you make sure that you have the Python package `codecov` installed, then Travis will automatically send any made coverage reports to CodeCov.

Additionally, one can make a ``.codecov.yml`` file in the repo root directory (like the ``.travis.yml`` file).
Here, one can specify the different options that CodeCov needs to take into account, and how you want the code coverage to be reported on the repo.
Using this, it is also possible for CodeCov to FAIL a commit if its coverage does not meet a specified threshold (currently, this is not done in the ``.codecov.yml`` file).
For example, you can make a commit fail if the code coverage of the entire package falls below 95%, or if the code coverage of the made changes is below 90% (and so on).
This can be extremely useful when you have an open-source package and others make pull requests to your package, while it also enforces you to keep all your tests up-to-date.

