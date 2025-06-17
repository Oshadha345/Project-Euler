def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(limit):
    """Generate Fibonacci numbers up to a given limit."""
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

def sum_of_multiples(limit, multiples):
    """Calculate the sum of all multiples of given numbers below a limit."""
    return sum(x for x in range(limit) if any(x % m == 0 for m in multiples))

def largest_prime_factor(n):
    """Return the largest prime factor of a given number."""
    factor = 1
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factor = i
            n //= i
    if n > 1:
        factor = n
    return factor