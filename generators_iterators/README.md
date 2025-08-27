# Generators and Iterators

This directory demonstrates the use of iterators and generators in Python utilizing two main files: `main.py` and `simple_digits_iterator.py`.

## main.py

This script demonstrates the usage of various generator functions implemented in `simple_digits_iterator.py`. It performs the following actions:

- Prints digits from 0 to 4 using the `simple_digits_generator`.
- Computes and prints the squares of numbers from 1 to 5 using the `nos_square` generator.
- Outputs the Fibonacci sequence up to a specified number using the `myfib` generator, showcasing access to individual elements and continued iteration.

## simple_digits_iterator.py

This file contains generator function implementations that produce sequences of numbers:

- **simple_digits_generator(n):**
  - Yields digits from 0 up to `n-1`.

- **nos_square(num):**
  - Yields squares of numbers from 1 up to `num`.

- **myfib(n):**
  - Yields Fibonacci numbers starting from 0 up to a number `n`. The sequence continues, and you can utilize the generator to resume iteration.
