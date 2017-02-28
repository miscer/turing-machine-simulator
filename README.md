# Turing Machine Simulator

The program requires Python version at least 3.5.0. All commands below need to
be executed in the same directory as this file.

## Simulation

The `runtm.py` script can simulate a Turing machine as required by the
practical specification.

Instead of using a file for the input, the `-` character can be specified to
instruct the program to read the input from STDIN.

```
$ python3 -m runtm solutions/palindrome.txt -
$ python3 -m runtm solutions/palindrome.txt input.txt
```

## Analysis

Analysis for each of the solutions is implemented as a separated script which
outputs CSV. They can be executed like this:

```
$ python3 -m analysis.sort
```

## Tests

Pytest is required to run the tests. To install it on the lab machines, you will need to use virtualenv.

```
virtualenv-3.5 venv
source venv/bin/activate
pip install pytest
```

Then tests can be run using

```
python -m pytest solutions
python -m pytest turingmachine
```
