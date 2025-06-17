def even_fibonacci_sum(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total

if __name__ == "__main__":
    result = even_fibonacci_sum(4000000)
    print(f"The sum of the even-valued terms in the Fibonacci sequence not exceeding four million is: {result}")


