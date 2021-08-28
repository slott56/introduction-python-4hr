###################################
Introduction to Python Programming
###################################

==============
Steven F. Lott
==============

Part 1 -- Getting Started: Python setup, Jupyter Lab


Agenda
===============

1. Installing Python

#. Virtual Environments and the Python "Ecosystem"

#. Installing Jupyter Lab (and why this is good)

#. Getting Started with Jupyter

#. Python Targets and run-times


1. Installing Python
====================

Your OS may have Python.

If it does, ignore it.

**Never** use the OS Python.

**Always** install your own fresh, new Python.

.. container:: incremental

    If you've already downloaded from https://www.python.org/downloads/
    that's okay. You can safely ignore it.

Installing Python
=================

Don't use https://www.python.org/downloads/

Why not?

Many large data science packages are very difficult to build.

You'll need extra help.

Extra help in the form of **conda**.

Installing CONDA
================

The best path forward is to install **conda** first.

Then use **conda** to install Python and other packages.

Two variants.

- Miniconda is a tiny thing that can build anything. A small, fast download.

- Anaconda is everything you may ever want. But. A huge download.

Start Here
==========

https://docs.conda.io/en/latest/miniconda.html

Find a Miniconda installer for your OS. Start downloading it now.

Use the downloaded installer to build **conda**.

Once you have **conda** you can manage virtual environments.

Which raises the question: "What is a virtual environment?"

.. container:: incremental

    (I'll talk about virtual environments while you wait for the download to finish.)

2. Virtual Environments and the Python "Ecosystem"
==================================================

In the olden days we used to install one copy of Python on one server.

- More-or-less part of the OS.
- Little flexibility.
- Shared by many users.

This was tolerable when computers were large, expensive, and rare.

It's inappropriate when everyone has their own laptop.

The Python Environment
======================

Python's environment has a (very) few things.

- The Python run-time: a program named ``python`` (or ``python.exe``).

- Some libraries and shared object files.

- The (large) standard library.

- Your site-specific add-on packages.

One environment, however, is rarely suitable.

Multiple Python Environments
============================

When a new version of a package is released...

Problem:

    You need to test.

    And.

    You don't want to break what you have.

Solution:

    You need multiple environments.

Conda and Virtual Environments
==============================

When you install **conda**, it gives you a new ``conda`` command.

(You will need to stop and restart any terminal windows.)

**conda** sets a new prompt prefix: ``(base)``

**Terminal** prompts will look like this:

::

    (base) slott@MacBookPro-SLott ODSC-Live-4hr %

The ``base`` conda virtual environment is active.

Installing A New Virtual Environment
====================================

Once you have the ``conda`` command, you can build Python and any Python package.

You do this by creating a new virtual environment at the terminal prompt:

::

    conda create -n demo1 python=3.9

You'll get a display of what needs to be downloaded and installed.

Then...

::

    Proceed ([y]/n)?

Activating A Virtual Environment
================================

Once Conda has built the environment, you need to activate it.
(I forget to do this all the time.)

::

    conda activate demo1

You'll often have many environments. What are they called?

::

    conda info --envs

Copying a Virtual Environment
=============================

Create a YAML file with the list of packages to install.

::

    conda list -e &amp;gt;environment.yml

Create a new environment from someone's export

::

    conda create -n team-env --file environment.yml

Getting Started Recap
=====================

1.  Download and Install Miniconda. https://docs.conda.io/en/latest/miniconda.html

2.  Create a new virtual environment.

    ::

        conda create -n name python=3.9

3.  Activate the virtual environment.

    ::

        conda activate name

You can manage this environment without too much brain scrambling.

Terminal Prompts
================

Yes. This is all done at the Terminal prompt.

That's not always obvious.

We get used to IDE's and other wrappers around our OS tools.

Other Virtual Environment Managers
==================================

**conda** is one of many solutions.

It's the best for scientists because it builds the BIG packages like scikit-learn.

It's fine for everyone else because it's consistent across all platforms.

**venv** is built-in, but **conda** is better for a lot of applications.


Do Not Uninstall OS Python
==========================

Do Not Uninstall the OS Python. It's part of the OS.

Do not attempt to upgrade or install anything new into the OS Python.
This usually requires elevated privileges.

You will (eventually) have a lot of old Python versions.
You can safely ignore them.

Avoid Homebrew
==============

The Homebrew approach to installing Python leads to working with elevated privileges.

It doesn't help (much) with complex AI/Machine Learning/Data Science packages.

If you started with this, you can safely ignore it and use **conda**.

Don't try to uninstall homebrew or a homebrew-created Python.

3. Installing Jupyter Lab
=========================

There are a lot of integrated development environments (IDE's) for Python.

Jupyter Lab provides a controlled execution environment.

- Great for exploration.
- Can create slide decks.
- Can create tidy PDF final reports.

It's **ideal** for science and acceptable for many other things.

The Install Command
===================

Since you have **conda** you can do this:

::

    conda install jupyterlab

This will add Jupyter Lab to your current virtual environment.

Do this now. (Be sure to answer "y" to the proceed? question.)

.. container:: incremental

    I'll talk about why Jupyter is so great while this downloads.

Why Jupyter Is So Great
=======================

You have a spreadsheet-like environment.

Cells with data.

Cells with expressions based on the data.

A chain of dependencies among the cells.

Change a cell, evaluate all the cells that follow: update the notebook.

What It Looks Like
==================

1.  Start the Lab Server.

    ::

        (python4hr) server dir % jupyter lab

2.  When the browser opens, build your notebook or module or whatever.

I'm going to launch the lab now...

Watch
=====

Enter expression like ``355/113`` in a cell.

Hit the ► button and computation.

We'll come back to this in the next sections of the course.


Jupyter Lab Recap
=================

1.  Install Jupyter Lab.

    ::

        conda install jupyterlab

2.  Start the lab server.

    ::

        jupyter lab

Do your programming in the browser. Mostly by creating notebooks.

4. Getting Started with Jupyter
================================

1.  We installed **conda**.

2.  **conda** at the terminal prompt installed Python and Jupyter Lab.

3.  ``jupyter lab`` at the terminal prompt to start a lab server.

4.  Click the Notebook Icon in the browser to create a notebook.

You can also interact with iPython directly via a console. (We'll come back to this, later.)

Important
=========

Python is a programming language.

Jupyter Lab is not a simple code editor.  It's a run-time environment.

There are three kinds of cells in a notebook.

-   Code. This is Python. The notebook evaluates these and the resulting object is displayed.

-   Markdown. This is text. The notebook formats these.

-   Raw. The notebook ignores these.

The Notebook Concept
====================

The default notebook mode is biased toward analysis and exploration.

Think of a lab notebook where you record your experiments.

(You can create libraries and apps, but we won't focus on this yet.)

You have the **full** Python language available to you.

You can do **anything**.

A Small Example
===============

Let's look at some calculator-like features.

Want to compute the volume of an irregular tetrahedron.

..  math::

    V = \frac{a^3}{6 \sqrt 2}

Sides vary: 48, 36, and 51 inches. We need to take an average.

Also. 231 cubic inches = 1 gallon (Sorry. American Units make no sense.)

What to do?
===========

Put the stuff we know into cells:

-   :math:`V = \frac{a^3}{6 \sqrt 2}`

-   Various values of :math:`a` that need to be averaged.

Add computations in cells.

Notebook Time
=============

Here's a document exported from the notebook, turned into a slide deck.

`compute_1.html <compute_1.html>`_

Change the measurement values. Recompute. This is fun.


A Bigger Example
================

I'll build a notebook to explore the Collatz Conjecture.

We have the HOTPO function, :math:`h(n)`.

..  math::

    h(n) = \begin{cases}
    \frac{n}{2}& \text{if } n \text{ is even},\\
    3n+1& \text{if } n \text{ is odd}
    \end{cases}

If we appy this iteratively, :math:`h(h(h( ... h(n))))`, is the result always 1?

Notebook Time
=============

I'll skip over some Python details to show how a notebook works.

::

    def h(n: int) -> int:
        if n % 2 == 0:
            return n // 2
        else:
            return 3 * n + 1


::

    def iterate_from(n: int) -> None:
        print(n)
        while n != 1:
            n = h(n)
            print(n)

Notebook Time
=============

Here's a document exported from the notebook, turned into a slide deck.

`collatz_1.html <collatz_1.html>`_

5. Python Targets and run-times
===============================

The notebook is fun, but, what if you have other platform ideas?

- Web server?

- Interactive client on a desktop?

- Interactive mobile client?

- Intenet of Things?

The Notebook
============

Before looking at other deployment options...

The notebook is very useful, even for "production."

Especially in business analysis (also called decision support).

It makes assumptions visible and lets users tweak them.

The resulting document is pure text and can be archived in a git repository.

Web Servers
===========

Big apps like Instagram use Python for their web servers.

You'll want a framework (like Flask.)

Or. If you're using Amazon, you'll want to use their Zappa version of Flask.

You'll be developing in an IDE like PyCharm instead of a notebook.

Desktop App
===========

You'll use a desktop GUI widget framework like PyQt or wxPython.

You'll be developing in an IDE like PyCharm in addition to a notebook.

You'll have to work out a deployment strategy to distribute the app.

Mobile Client
=============

You'll want a mobile-based framework like BeeOS or Pythonista.

You'll be developing in an IDE like PyCharm instead of a notebook.

You'll have to work out a deployment strategy to distribute the app.

Internet of Things
==================

You'll be using a Raspberry Pi or a Circuit Playground Express.

You won't need a very sophisticated IDE, but it can help.

    I'm a fan of creating mock test libraries and using PyCharm.

You'll be downloading the software onto the boards for testing and deployment.


Common Theme?
=============

Not very many common themes. These are wildly distinct environments.

I suggest starting with a notebook to understand the problem and the data.

Then work on your target deployment once you have core algorithms and data structures working.

Make a firm distinction

-   essential problem-domain objects (which never change.)

-   solution-domain objects (notebook, web, desktop, IoT, etc.)

Summary
=======

- Download conda (Miniconda or Anaconda)
- Build virtual environments.
- Use JupyterLab to get started.

Questions?
===========

We'll start at the top of the hour with Part 2, **Built-in data structures: list, set, dictionary, tuple**

BTW. The next two sections will be done entirely in Jupyter Lab.
