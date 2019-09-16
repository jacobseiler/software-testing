Maintaining tests
=================
Once you have written tests for your code, you have jumped the biggest hurdle.
However, you are not done yet.
While writing tests for your code is extremely important, it is just as important to maintain them and the code they are testing.
Below, we give an overview of the different ways you can make maintaining tests/code easier; and make them more efficient.

But first, you might be wondering why maintaining code and tests is so important.
After all, you have written your tests; everything works properly; and you are the only one making changes to the code (or even use it).
The reason is pretty simple: Unlike the old classics like C; C++; and Fortran, which have proven to stand the test of time, Python is a very rapidly evolving programming language.
Besides Python 2.7 (which should have never existed anyway and will finally be deprecated on the 1st of January 2020), no single minor Python version has survived for two years before being succeeded (`source <https://www.python.org/doc/versions/>`_).
Not only that, but the language itself is also continuously becoming more and more popular, as it is currently the third most popular programming language, after C and Java (`source <https://www.tiobe.com/tiobe-index/>`_), and might overtake them fairly soon.
What this means is that a brand-new, state-of-the-art Python script/package today, could quickly become an outdated one within just a few years.
There is nothing worse than coming back to an old piece of code a few years later, and finding that it has numerous bugs and is completely incompatible with your current environment.


Code requirements
=================
Almost every Python code relies on a collection of external third-party packages, with NumPy probably being the most common one.
This means that if anyone wants to use your code, they need to have these third-party packages installed.
The most common thing to do, is to write all of these packages down in a file called ``requirements.txt`` and include this on the GitHub repo.
If your code is a package, you can write your ``setup.py`` file such that it automatically ensures that the list of requirements in this file is satisfied.

As easy as that may sound, there are two very common mistakes being made regarding the specification of a code's requirements, both greatly hampering the maintainability and usability of a code:

- Not specifying all requirements that a code needs.
  This happens mostly due to them being so commonly used (like NumPy or Matplotlib) or because they are already satisfied by another requirement;
- Not specifying minimum versions for most (all) requirements.

Not specifying all requirements is dangerous, regardless of the reason for it (although the latter reason is much more dangerous).
An easy way to check what your requirements should be, is to go through every Python file and check your imports.
Unless you are importing from either a builtin package (like ``os``; ``sys``; ``logging``; ``time`` etc.) or from a Python file contained in the same repo, it is a third-party requirement and you should specify it.
Do not rely on a different requirement covering it for you.

An example of this would be the following with the Matplotlib (MPL) package:

1. My code requires NumPy and MPL;
2. MPL requires NumPy;
3. Installing MPL will therefore install NumPy;
4. Thus, requiring MPL would give me NumPy as well;
5. So, NumPy does not need to be specified as a requirement.

This reasoning is wrong because one cannot guarantee that MPL will require NumPy for the rest of eternity (although I would not be surprised if it did).
If somehow MPL would get rid of its reliance on the NumPy package and therefore removes it from its requirements, any code that requires both MPL and NumPy using this reasoning will no longer work.
This means that its maintainer will now have to make an update to the code stating that it does require NumPy, which could have been avoided altogether.
In case of released packages, it could literally render all currently released versions unusable (as their requirements cannot be changed anymore), especially if the second mistake from above was made as well.
Simply put, if your code uses a specific third-party (so, not builtin) package, then you must specify it as a requirement.

It is also important to specify the minimum version of most, if not all, requirements.
This ensures that when the user has all packages installed that were specified by the requirements, they also have the same functionality as you expect them to have.
A good starting point for figuring out the minimum required versions, is to check what the versions are that work and simply use these as your minimum required versions.
This will work perfectly fine, even if it is not totally fair to do (it may force unnecessary package updates or cause unnecessary incompatibilities).

Unlike the previous mistake, this mistake is much harder to track down once somebody encounters it.
For example, let's say that you have a code that requires AstroPy 3.0 or later, but you only specified the package as a requirement without a minimum version.
Now, when somebody tries to use your code using AstroPy 1.x, they will be convinced that they satisfy all requirements, as they already have AstroPy.
Then, when using your code, it will attempt to use a functionality that had not been implemented yet in AstroPy 1.x, and it will raise an error.
For the user, this error will not provide any indication that their requirements are outdated, and it will not provide you with much information either about what the minimum version should have been.
Encountering a problem like this is extremely annoying and frustrating for both the user and the maintainer.

It can however sometimes be a bit hard to figure out whether your minimum versions are still up-to-date.
Usually, we update our local environments to newer versions even though that was not necessary.
Specifying minimum versions that are much later than actually required, can cause problems with packages that have a maximum required version for the same package.
Therefore, be a bit lean with what your minimum required versions are, but ALWAYS specify them.


Pytest plugins
==============
We have learned about using pytests for testing your code.
Here, we introduce a few plugins to ``pytest`` that can make it more efficient and allow for easier maintainability.
In order to use a ``pytest`` plugin, one will have the install it first using ``pip install pytest-xxx``, like ``pip install pytest-cov`` for the coverage plugin for ``pytest``. 

pytest-mpl
----------
- Provides a set of tools that allows for figures created with Matplotlib to be tested more easily;
- These tools include the option to fully render a figure without having an X-window (required for cloud computing); comparing figures with each other on a pixel-by-pixel or rough format basis; and more;
- It can be enabled by adding the ``--mpl`` option to pytest or by adding it to the ``setup.cfg`` file;
- Extremely helpful for testing packages that generate lots of figures.

pytest-pep8
-----------
- Pytest can also automatically test every file for PEP8-compliance with the ``pytest-pep8`` plugin;
- This can be enabled by adding the ``--pep8`` option to pytest;
- With this plugin enabled, ``pytest`` will automatically fail any file that is not PEP8-compliant (which therefore fails the entire test run as well);
- Currently, the scripts in this repo are not PEP8-compliant, as you will see when adding the ``--pep8`` option.

pytest-cov
----------
- By using the ``pytest-cov`` plugin, one can check which lines in a package or set of scripts are currently covered by all pytests;
- Instead of executing ``pytest``, executing ``pytest --cov --cov-report=term-missing`` will automatically track coverage over all pytests and print out the results later;
- Optionally, one could add the ``--cov-branch`` option to also get a report on branch coverage (which was explained by Will);
- It is also possible to write these options into a ``setup.cfg`` file, such that they are automatically used whenever ``pytest`` is executed;
- In the same file, one can also write options for the ``pytest-cov`` plugin itself (or ``coverage.py``, as that is what the package is actually called that runs it in the background).


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

One way of dealing with some of these issues, is by using a CI service as will be introduced later.
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
After running your tests, it is possible to upload the coverage report to CodeCov.
CodeCov is a coverage service, that automatically tracks the code coverage of a repo.
This allows for much easier overviews of the status and coverage of your own code.

Getting started with CodeCov is really easy (and we will do it during this workshop).
The only thing that is necessary to do, is go to https://codecov.io, login with your GitHub account and activate the repo you want to do code coverage for.
After that, when you install the Python package ``codecov``, you can send coverage reports to CodeCov using the same command (i.e., ``codecov``)
If you are using Travis CI, you can add two lines to your ``.travis.yml`` file with::

    after_success:
    - codecov

This will cause Travis to automatically send any made coverage reports to CodeCov (see discussion on CI services).

Additionally, one can make a ``.codecov.yml`` file in the repo root directory.
Here, one can specify the different options that CodeCov needs to take into account, and how you want the code coverage to be reported on the repo.
Using this, it is also possible for CodeCov to FAIL a commit if its coverage does not meet a specified threshold (currently, this is not done in the ``.codecov.yml`` file).
For example, you can make a commit fail if the code coverage of the entire package falls below 95%, or if the code coverage of the made changes is below 90% (and so on).
This can be extremely useful when you have an open-source package and others make pull requests to your package, while it also enforces you to keep all your tests up-to-date.


Continuous Integration (CI)
===========================
Another important part of maintaining your code/tests, is by using a continuous integration (CI) service, like Travis CI (https://travis-ci.com).
A CI service allows you to execute a series of specified tests on the GitHub repo, every time a commit (or set of commits) is being pushed.
However, unlike executing tests on your own computer, a CI service can do this using far more flexibility and this can be integrated into your GitHub repo.
It can even be set up such that it performs tests on a regular basis using CRON jobs (explained later on), which greatly increases the code's maintainability.

What is a CI service?
---------------------
So, what does a CI service like Travis CI do exactly?
Once set up properly for your GitHub repo, Travis will be notified by GitHub every time a push has been made.
When a push was made, Travis will automatically set up a collection of environments (as specified by the ``.travis.yml`` file, like the ``.codecov.yml`` file), clone the repo and execute a bunch of scripts.
These scripts can range from simply installing all the requirements and doing the pytests; to checking if a repo can be packaged up properly; to even generating and uploading entire webpages.
It allows for many pipelines to be automated.
Here, we just focus on getting our pytests done, which requires the simple ``.travis.yml`` file in this repo.

One thing to remember when using a CI service, is that it starts off completely blank.
This means that you have to specify everything that is required to execute the tests.
The benefit of this is that it makes it really easy to spot if you forgot to add a requirement somewhere (as a test will crash or fail), or made an assumption about the state of the system (for example, Windows uses 32-bit and 64-bit versions of its OS, while Linux and Mac OS-X solely use 64-bit versions).
It also allows you to check your code using OSs or Python versions that you do not have access to (especially in the case of the former).

Another cool thing about using a CI service, is that they can report their status back to GitHub on the specific commit they used, or even automatically send their reports to services like CodeCov.
This, for example, allows for a CI service to FAIL a commit (like CodeCov can) if one of their tests failed, informing you immediately that there is something wrong with that commit.
It is generally speaking a good idea to have at least one CI service active for your GitHub repo at all times, especially if it is something that will be open-source.
Travis CI is one of the few CI services that allows for private repos to be tested as well for no cost, although with a reduced capacity.
