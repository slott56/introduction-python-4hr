Essential Computation
=====================

Volume of a tetrahedron.

\\[ V = \\]

Real tetrahedron is irregular with three nearly-equal measurements.

.. code:: ipython3

    a_1 = 48
    a_2 = 36
    a_3 = 51

.. code:: ipython3

    a = (a_1 + a_2 + a_3) / 3

.. code:: ipython3

    a




.. parsed-literal::

    45.0



.. code:: ipython3

    from math import sqrt

.. code:: ipython3

    V = a**3 / (6*sqrt(2))

.. code:: ipython3

    V




.. parsed-literal::

    10739.18423927069



.. code:: ipython3

    V / 231




.. parsed-literal::

    46.489975061777876



.. code:: ipython3

    round(Out[7])




.. parsed-literal::

    46



