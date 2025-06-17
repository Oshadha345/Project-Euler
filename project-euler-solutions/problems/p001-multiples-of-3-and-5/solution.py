def arithmetic_sum(n):
    """Calculate the sum of the first n natural numbers."""
    return n * (n + 1) // 2
    

def sum_of_multiples(limit):
    """Calculate the sum of all multiples of 3 or 5 below a given limit.

    Args:
        limit (int): The upper limit (exclusive) to consider for multiples.

    Returns:
        int: The sum of all multiples of 3 or 5 below the limit.
    """
    
    num_3 = limit // 3
    num_5 = limit // 5
    num_15 = limit // 15
    
    sum = 3 * arithmetic_sum(num_3) + 5 * arithmetic_sum(num_5) - 15 * arithmetic_sum(num_15)
    # The sum of multiples of 3 and 5 below the limit is:
    # sum of multiples of 3 + sum of multiples of 5 - sum of multiples of 15 (to avoid double counting)
    
    return sum 



if __name__ == "__main__":
    result = sum_of_multiples(1000)
    print(f"The sum of all the multiples of 3 or 5 below 1000 is: {result}")