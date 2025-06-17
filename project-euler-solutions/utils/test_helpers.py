import os
import sys

# Ensure the project directory is in the Python path
project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

def assert_equal(actual, expected):
    """Asserts that the actual value is equal to the expected value."""
    assert actual == expected, f"Expected {expected}, but got {actual}"

def run_tests():
    """Runs all the test cases for the Project Euler solutions."""
    # Example test cases for Problem 1
    from .p001_multiples_of_3_and_5.solution import solution as p001_solution
    assert_equal(p001_solution(), 233168)

    # Example test cases for Problem 2
    from .p002_even_fibonacci_numbers.solution import solution as p002_solution
    assert_equal(p002_solution(), 4613732)

    # Example test cases for Problem 3
    from .p003_largest_prime_factor.solution import solution as p003_solution
    assert_equal(p003_solution(13195), 29)

if __name__ == "__main__":
    run_tests()