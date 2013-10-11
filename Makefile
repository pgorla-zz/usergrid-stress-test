.PHONY: clean test

all: clean test

clean:
	find . -name '*.pyc' -exec rm -f {}

test:
	python test_stress.py
