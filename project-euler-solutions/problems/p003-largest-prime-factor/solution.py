def largest_prime_factor(n):
    # Start with the smallest prime factor
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n

# Example usage
if __name__ == "__main__":
    number = 600851475143
    print("The largest prime factor of", number, "is", largest_prime_factor(number))