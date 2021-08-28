.PHONY: tests

slides : docs/index.html docs/part_1.html docs/collatz_1.html docs/compute_1.html docs/part_4.html

%.html : %.rst
	rst2s5.py $^ > $@

tests :
	python -m doctest src/collatz.py
	PYTHONPATH=src python -m pytest --cov=src --cov-report=term-missing
