# Largest Prime Factor

## Problem Statement

The goal of this problem is to find the largest prime factor of a given number. Specifically, you will be tasked with determining the largest prime factor of the number 600851475143.

## Explanation

A prime factor is a factor that is a prime number. To solve this problem, you will need to:

1. Identify all the prime factors of the given number.
2. Determine which of these factors is the largest.

## Approach

The approach to solving this problem involves:

- Starting with the smallest prime number (2) and checking if it divides the given number.
- If it does, divide the number by this prime factor and continue checking with the same prime until it no longer divides evenly.
- Move to the next prime number and repeat the process until the number is reduced to 1.
- The last prime factor used in the division process will be the largest prime factor.

## Example

For the number 13195, the prime factors are 5, 7, 13, and 29. Therefore, the largest prime factor is 29.

## Notes

- Ensure that your solution is efficient, as the number can be quite large.
- Consider edge cases, such as when the number itself is prime.

## Running the Solution

To run the solution for this problem, execute the `solution.py` script located in this directory. Make sure you have Python installed on your machine.

```bash
python solution.py
```

## Contribution

Feel free to contribute to this repository by adding more solutions or improving existing ones. Make sure to follow the coding standards and include appropriate documentation for your contributions.