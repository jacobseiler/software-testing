.. code:: rst

    |TRAVIS|
*Once you have your TRAVIS build running and your badge successfully added down the bottom of the README, you can use the above to add a shiny badge at the top of your repo.*


*************************************
ADACS + ASTRO3D Code Testing Workshop
*************************************

This repository contains materials for the ADACS + ASTRO3D Code Testing
workshop.

Fork the Repo
=============

You should first create a **fork** of this repo and clone the fork onto your
local machine.  This will allow you to make commits without affecting anybody
else.

You should also set the **upstream** repo of your fork to be **this** repo, 
``https://github.com/jacobseiler/software-testing``. Your ``.git/config`` file
should hence look like...

.. code:: bash

    [core]
        repositoryformatversion = 0
        filemode = true
        bare = false
        logallrefupdates = true
    [remote "origin"]
        # Your username goes instead of 'JohnDoe'.
        url = https://github.com/JohnDoe/software-testing
        fetch = +refs/heads/*:refs/remotes/origin/*
    [remote "upstream"]
        # Keep this as my username.
        url = https://github.com/jacobseiler/software-testing
        fetch = +refs/heads/*:refs/remotes/upstream/*
    [branch "master"]
        remote = origin
        merge = refs/heads/master

This setup will allow you to integrated any changes we make to this repo into
your own fork by executing ``git pull upstream master``.

Requirements
===========

* The workshop exclusively uses Python.  Specifically, Python >=3.6.  **If are still
  using Python 2, stop.  Python 2 will no longer be supported after January 1st
  2020.**
* ``codecov``
* ``numpy``
* ``pytest``
* ``pytest-cov``
* ``pytest-pep8``
* ``scipy``

These packages can by installed using ``pip install -r requirements.txt``.

Links to GitHub
---------------

A key to good testing is automation. During this workshop, we will be linking
our tests to `codecov <https://codecov.io/>`_ and `Travis <https://travis-ci.com/>`_.
We recommend heading to both of these sites, linking your GitHub account, and
having a bit of a poke around.  Get comfortable with the interface.

Accessing the Solutions
=======================

We don't have any!  The prompts and ideas for extensions codes we provided is
us just spitballing.  We don't have any hard and fast solutions for them.

If you want help though, we have some tips...


Badges
======
Adjust the URLs here to point to your own Travis badge!

.. code:: rst

  .. |TRAVIS| image:: https://travis-ci.com/jacobseiler/software-testing.svg?token=5c6Q56fcBuVVhRGKosZB&branch=master
    :alt: Travis Badge
    :target: https://travis-ci.com/jacobseiler/software-testing
