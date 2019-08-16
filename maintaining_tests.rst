PLUGINS
-------
pytest-cov:
- By using the `pytest-cov` plugin, one can check which lines in a package or set of scripts are currently covered by all pytests;
- Instead of executing `pytest`, executing `pytest --cov --cov-report=term-missing` will automatically track coverage over all pytests and print out the results later;
- It is also possible to write these options into a ``setup.cfg`` file, such that they are automatically used whenever `pytest` is executed;
- In the same file, one can also write options for the `pytest-cov` plugin itself (or `coverage.py`, as the package is actually called that runs it in the background);

pytest-pep8:
- Pytest can also automatically test every file for PEP8-compliance with the `pytest-pep8` plugin;
- This can be enabled by adding the `--pep8` option to pytest, or by adding it to the ``setup.cfg`` file;
- With this plugin enabled, pytest will automatically fail any file that is not PEP8-compliant (which therefore fails the entire test run as well);
- Currently, the scripts in this repo are not PEP8-compliant, as you will see when adding the `--pep8` option;


Coverage
--------
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


One way of dealing with some of these issues, is by using a CI (continuous integration) service like Travis CI.
By using a CI service, one can perform all tests using all combinations of operating systems, architectures (sometimes at least) and Python versions.
If you are going to make your code publicly available (especially if it is going to be written up in a package), it is a really good idea to have at least one CI service active.

