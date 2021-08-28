Collatz Conjecture
==================

Step 1.
-------

Define a function

.. code:: ipython3

    def h(n: int) -> int:
        if n % 2 == 0:
            return n // 2
        else:
            return 3 * n + 1

Step 2.
-------

Test the function.

.. code:: ipython3

    h(10) == 5




.. parsed-literal::

    True



.. code:: ipython3

    h(5) == 16




.. parsed-literal::

    True



Step 3.
-------

Iterate a few times.

.. code:: ipython3

    h(5)




.. parsed-literal::

    16



.. code:: ipython3

    h(16)




.. parsed-literal::

    8



.. code:: ipython3

    h(Out[5])




.. parsed-literal::

    4



.. code:: ipython3

    h(Out[6])




.. parsed-literal::

    2



Step 4.
-------

Define an iteration function that prints a result.

.. code:: ipython3

    def iterate_from(n: int) -> None:
        print(n)
        while n != 1:
            n = h(n)
            print(n)

.. code:: ipython3

    iterate_from(16)


.. parsed-literal::

    16
    8
    4
    2
    1


.. code:: ipython3

    iterate_from(15)


.. parsed-literal::

    15
    46
    23
    70
    35
    106
    53
    160
    80
    40
    20
    10
    5
    16
    8
    4
    2
    1


