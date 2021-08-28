###################################
Introduction to Python Programming
###################################

==============
Steven F. Lott
==============

Part 4 -- Tooling and Good Practices

Agenda
======

1. Base Python Runtime and Virtual Environment Manager

2. Jupyter Lab

3. IDE

4. Testing

5. Multi-Environment Testing

6. Documentation

7. Deployment

1. Base Python Runtime and Virtual Environment Manager
======================================================

See Part 1.

Use **conda**.

1. Download Miniconda (or the full Anaconda if you're a scientist)

2. Install Conda (or Anaconda)

3. Use ``conda create`` to create a Python environment

4. Use ``conda activate`` to activate a environment

Why Conda?
==========

Python comes with ``venv``, plus there are many others.

Conda is particularly good a building large scientific packages.

The ``conda`` script is consistent on POSIX (Linux and macOS) as well as Windows.

Why Use Another?
================

Python comes with ``venv``.

If

- you can install a Python binary from https://www.python.org/downloads/

- you'll *never* build a binary of any kind

You don't need **conda**.  ``venv`` will do nicely.

Why Use Virtual Environments?
=============================

One environment is never enough.

Open source software in general is in a constant state of flux.

You'll always need to test against newer versions of packages, libraries, frameworks.

Python changes on a regular cadence. See https://www.python.org/dev/peps/pep-0619/

Docker Images
=============

Don't know how many folks intend to use docker images. I can recommend this path.

You can often find docker images with Python installed.

Example ``ubuntu:latest``, ``debian:latest``, ``python:3.9``

::

    docker pull python
    docker run -it --rm -v "$PWD" python:3 python your-script.py

Summary
=======

Use a virtual environment manager.

Ideally. Use **conda** to build Python for you.

Otherwise. Download the Python binary and use whatever virtual environment makes you happiest.

2. Jupyter Lab
==============

Use **Jupyter Lab**

1.  Install it in your current virtual enviroment.

    ::

        conda install jupyterlab

2.  Star the lab server.

    ::

        jupyter lab

3.  Create a notebook.

Why Use JupyterLab?
===================

It's really cool and friendly.

Why Not Use Interactive Python?
===============================

It's very low overhead.

::

    (python4hr) ODSC-Live-4hr % python
    Python 3.9.6 (default, Aug 18 2021, 12:38:10)
    [Clang 10.0.0 ] :: Anaconda, Inc. on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 355/113
    3.1415929203539825
    >>>

It's a bare Read-Execute-Print Loop (REPL).

"Production" Use -- i.e. Automation
===================================

Consider your use cases.

-   Analysis? Decision-Support? Science?

    Notebook. Users can tweak assumptions and do "what-if" analysis.

-   Automation? Web Server? IoT Application? Mobile Application?

    Deployed App. Admins can change configuration.

Development
===========

Python is designed to be used interactively.

-   The command-line REPL is a first-class feature, not an add-on.

Use Python interactively to explore algorithms and data.

-   Don't write code, run the compiler, run the debugger, and see what broke.

-   Write code and see what happens.

Can't emphasize this enough
===========================

Been writing Python code for 20 years.

A REPL prompt open in a terminal window (or the IDE) at **all** ties.

Use it as a desk calculator.

Did a weekly in-house webcast for years from a jupyter notebook.

But. What if it's complex?
==========================

Outside talks like these, it's always complex.

You'll often be creating your own modules and libraries.

You can provide users with a notebook that has ``imports`` all set up and ready to roll.

You can give them super-handy libraries of ready-to-use functions.

Summary
=======

The Jupyter Lab is very handy.

3. IDE
======

When you're going to be writing Python apps, libraries, modules, frameworks, scripts, etc.

Any text editor will do.  **Any**.

.. container:: incremental

    Except notepad on Windows. Never use notepad.

IDE Examples
============

- Anaconda includes Spyder. It's Scientific. https://www.spyder-ide.org

- I like PyCharm community edition. https://www.jetbrains.com/pycharm/

- VS code is popular. https://code.visualstudio.com/docs/languages/python

- For IoT, you'll also be using ``screen``, or something similar.

There are -- maybe -- 20 more choices. All good. All.

Why So Many IDE's?
==================

Python is simple.

- Simple interactive run-time.

- Simple text language.

**No compile/build/archive tool overhead.**

Minimal debugging and packaging complexity.

No Tool Overhead
==============================

A lot of complexity in Java, C, C++, etc., comes from the compiler.

And the archiver to make JAR's (or .ar or whatever).

And the linker to make an executable app from .o files and .ar.
(or .java and .jar)

None of this in Python.

But Wait! You Say
=================

I used ``python -m pip install whatever``

It downloaded a "wheel" ``whatever.whl``.

Isn't that tooling overhead? Just like a JAR file?

It's Handy. But No.
=================================

Much Python software is available as a "wheel" or "egg".

This is not **required**.

You never need to make these.

This tooling is outside the language and only required if you package things for PyPI.

Debugging?
==========

The ``pdb`` Python debugger is part of the distribution.

Feel free to use it.

(I add ``print()`` functions. I don't often use the debugger.)

Packaging?
==========

When you've got a great library/package/framework/tool/whatever...

You'll want to put it on PyPI for others to share.

Then you'll get involved in "distutils" and "twine".

Don't start there, though. First, get stuff to work.

Organization
============

::

    src
        collatz.py

    tests
        test_collatz.py

    docs
        ... created by sphinx

    README
    requirements.txt
    pyproject.toml

Follow Along
============

Make some directories

-   ``src``
-   ``test``
-   ``docs``

Create a ``collatz.py`` file in src.

We'll put some code in it later.

Important
=========

Flat is better than nested.

Don't create one-file-per-class. This is a silly approach designed to help the compiler.

Don't create lots and lots of nested directories. They don't help much.

You don't need much. A single ``myscript.py`` is acceptable. Really.

Summary
=======

Any text editor will be good.

There's not much that's required.

You want syntax coloring, ready access to Python prompt and command line.

Don't sweat PyPI packaging and distribution.

4. Testing
==========

Unit testing and integration testing are really important.

Really important.

    Software features that can't be demonstrated by automated tests simply don't exist.

    `Extreme Programming Explained`, Kent Beck

.. container:: incremental

    What do we do?

Testing Approach
================

TDD -- Test-Driven Development is your friend.

To the extent possible, write test cases first.

Fill in working code later to make the tests pass.

Testing Tools
==============

-   ``doctest`` -- part of Python's Standard Library.

-   ``pytest`` -- an add-on, but REALLY useful.

-   ``unittest`` -- part of the Standard Library, but harder to use.

-   ``unittest.mock`` -- Mock objects to permit unit testing.

-   ``coverage`` -- an add-on. You'll want this, also.

Using Doctest
=============

The ``doctest`` tool scans a file, looking for ``>>>`` examples.

It runs the ``>>>`` line(s) of code.

Compares them with the lines that follow.

My File: src/collatz.py
=========================

::

    def hotpo(n: int) -> int:
        """
        >>> hotpo(10)
        5
        >>> hotpo(5)
        16
        """
        if n % 2 == 0:
            return n // 2
        else:
            return 3 * n + 1

Running Doctest
===============

::

    % python -m doctest src/collatz.py

No output? No failures.

Want details? Add ``-v``.

::

    % python -m doctest -v src/collatz.py

Using Pytest
============

First. Install it ``conda install pytest``.

The ``pytest`` tool looks for a ``tests`` directory.

Inside that directory, it looks for files with names starting with ``test*.py``.

Within those files, it looks for test cases.

-   Function named ``test...``.

-   Subclass of ``unittest.TestCase``.

My File: ``tests/test_collatz.py``
==================================

::

    import pytest
    from collatz import hotpo

    def test_hotpo():
        assert 5 == hotpo(10)
        assert 16 == hotpo(5)

Running Pytest
===============

::

    % PYTHONPATH=src python -m pytest

    ===================== test session starts =====================
    platform darwin -- Python 3.9.6, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
    rootdir: /Users/slott/Documents/Writing/Python/ODSC-Live-4hr
    plugins: anyio-2.2.0
    collected 1 item

    tests/test_collatz.py .                                 [100%]

    ====================== 1 passed in 0.02s ======================

Wait. What's that command again?
================================

Code is in a ``src`` directory.

To make code in ``src`` visible:

-   Package and install. Ugh.

-   Put ``src`` directory into the ``PYTHONPATH`` environment variable
    ::

        PYTHONPATH=src python -m pytest

Using Unittest
==============

::

    import unittest
    from collatz import hotpo

    class TestHotpo(unittest.TestCase):
        def test(self):
            self.assertEqual(5, hotpo(10))
            self.assertEqual(16, hotpo(5))

..  container:: incremental

    Wordy.

Mocking
=======

We create mock collaborators to test a class in isolation.

It's a stand-in that has just enough behavior to not crash the test.

Usually filled with known, fake answers.

::

    >>> transform = Mock(return_value=42)
    >>> transform(1)
    42

More of src/collatz.py
======================

::

    def iterate_from(n: int) -> Iterator[int]:
        yield n
        while n != 1:
            n = hotpo(n)
            yield n

Depends on ``hotpo()``. Isolation requires a ``Mock``.

Creating a Mock
===============

::

    import pytest
    from unittest.mock import Mock, call

    @pytest.fixture
    def mock_hotpo(monkeypatch):
        m = Mock(name='mock hotpo', side_effect=[4, 2, 1])
        monkeypatch.setattr(collatz, 'hotpo', m)
        return m

Using A Mock
============

::

    def test_iterate_from(mock_hotpo):
        results = list(collatz.iterate_from(42))
        assert results == [42, 4, 2, 1]
        assert mock_hotpo.mock_calls == [
            call(42),
            call(4),
            call(2)
        ]

Design for Testability
======================

Helps to follow the SOLID design principles.

The dependency between ``iterate_from()`` and ``hotpo()`` is a design problem.

-   Not following Open/Closed Principle or Dependency Inversion Principle

Requires monkeypatching the module for a test.

Coverage
========

The topic of test case coverage is huge.

- Cover all lines of code?

- Cover all paths through the logic?

- Cover all the important integration interfaces?

A Simple Approach
=================

Strive for 100% code coverage.

::

    conda isntall pytest-cov

::

    PYTHONPATH=src python -m pytest --cov=src \
        --cov-report=term-missing

Example Coverage Report
=======================

::

    ---------- coverage: platform darwin, python 3.9.6-final-0 -----------
    Name             Stmts   Miss  Cover   Missing
    ----------------------------------------------
    src/collatz.py      10      0   100%
    ----------------------------------------------
    TOTAL               10      0   100%

Testing Basics
==============

1.  ``doctest`` Start here. Use ``>>>`` examples everywhere.

2.  ``pytest`` Use this as your primary test engine.

3.  ``unittest.mock`` Buids mock objects. Good design reduces need for monkeypatching.

4.  ``coverage`` Install ``pytest-cov`` and it's integrated with ``pytest``.

..  container:: incremental

    Yes, there's more.

5. Multi-Environment Testing
============================

We'll always have multiple versions of packages on which we depend.

We'll need to test various versions of those packages with our code.

How do we do this?  **tox**

What tox does
=============

The **tox** tool build virtual environments.

And runs commands in each environment.

..  container:: incremental

    That's all.

..  container:: incremental

    But wow! is that handy

Install
=======

This isn't available through **conda**

::

    python -m pip install tox


Configuration
=============

There are two paths for configuration for **tox**

-   A ``tox.ini`` file.  This is simple.

-   A ``pyproject.toml`` file. This is more complete.

    -   But the syntax is confusing.

We'll focus on a simple ``tox.ini``.

tox.ini part 1
==============

Some generic overhead.

::

    [tox]
    minversion = 3.20.0
    skipsdist = True
    envlist = json-3-2-0,json-4-0-0


tox.ini part 2 -- General Environment
======================================

::

    [testenv]
    deps =
        pytest==6.2.4
        pytest-cov==2.12.0
        mypy==0.910
    setenv   =
        PYTHONPATH = {toxinidir}/src
    commands =
        python -m doctest --option ELLIPSIS src/collatz.py
        python -m pytest --cov=src --cov-report=term-missing
        mypy --strict --show-error-codes src

tox.ini part 3 -- Specific Overrides
====================================

::

    [testenv:json-3-2-0]
    deps =
        {[testenv]deps}
        jsonschema==3.2.0

    [testenv:json-4-0-0]
    deps =
        {[testenv]deps}
        jsonschema==4.0.0a6

Running Tox
==============

::

    % tox

Output from each command...

::

    ________________________ summary ________________________
      json-3-2-0: commands succeeded
      json-4-0-0: commands succeeded
      congratulations :)

The first run after a change populates a cache. After that, it's fast.

Summary
=======

You're going to have multiple test commands: doctest, pytest, mypy, pylint, etc.

Don't write a shell script.

Use ``tox`` to run the suite of commands.

Later, when you have multiple environments, tox can manage those, too.

6. Documentation
================

Easy.

Use Sphinx.

Steps
=====

1. Install sphinx:  ``conda install sphinx``.

2. Create a ``docs`` directory.  ``cd docs``.

3. Run ``sphinx-quickstart`` in ``docs`` to build the ``config.py`` for you.

4. Run ``make html`` to build HTML docs.

Writing
=======

You can write in Markdown or ReStructured Text (RST).

You can organize the files any way that makes sense.

-   You don't pile it all in one file.

-   Decompose like you decompose software.

You can use the ``..  automodule::`` directive to generate API reference documentation
from your source code.

Summary
=======

Use Sphinx.

It's how Python's internal documentation is produced.

Documentation comes from the source.

7. Deployment
=============

Are we there yet?

How do we deploy the app after we've written, tested, and documented it?

Deployment Choices
==================

-   Enterprise server apps

-   Desktop apps

-   PyPI Packages for apps/libraries/frameworks/modules/packages


Enterprise server apps
=======================

- A small script can ``git clone`` onto the servers and away you go.

- Docker images are popular.

- AWS Cloud Formation Templates to build server and ``git clone`` your app.

Desktop apps
============

-   Helps to build a platform-specific executable.

-   **py2app** and **py2exe** can help with this.

-   They package the Python run-time plus all the required packages

-   Docker images are popular for this.

PyPI Packages for the world to use
==================================

1.  Build a distribution kit.

2.  Test locally with **tox**.

3.  Put it on the PyPI test server.

4.  Make sure ``python -m pip install`` can install it.

Creating A Distribution Kit
===========================

This can be hellishly complex, depending on what your package contains.

In the most trivial cases (pure python)

1.  Write a setup.py

2.  Run ``python setup.py sdist``

Beyond that, there are a lot of details to get right.

CI/CD
=================

Continuous Integration / Continuous Deployment

You really want to automate this as much as possible.

-   Enterprise users often work with Jenkins.

-   GitHub allows you to include CI/CD commands in your repository.

You don't want to type commands manually to test, build, and deploy your code.

Summary
=======

For "simple" Enterprise cases, ``git clone`` is your friend.

For world-wide distribution via PyPI:

-   Simple pure Python projects have a simple source distribution

-   Anything else may involve platform-specific considerations

Wrap-up
=======

1. Base Python Runtime and Virtual Environment Manager

2. Jupyter Lab

3. IDE

4. Testing

5. Multi-Environment Testing

6. Documentation

7. Deployment

Questions?
==========



