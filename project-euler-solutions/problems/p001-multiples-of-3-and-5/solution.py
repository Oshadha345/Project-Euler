def sum_of_multiples(limit):
    return sum(i for i in range(limit) if i % 3 == 0 or i % 5 == 0)

if __name__ == "__main__":
    result = sum_of_multiples(1000)
    print(f"The sum of all the multiples of 3 or 5 below 1000 is: {result}")