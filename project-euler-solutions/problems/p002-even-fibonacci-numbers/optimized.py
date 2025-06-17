def even_fib(limit):
    
    sum = 2
    f = 2
    phi_cube = ((1 + 5 ** 0.5) / 2 ) ** 3
    
    while f <= limit:
        f = round(f * phi_cube)
        
        sum += f
    
    sum -= f
    
    return sum 

if __name__ == "__main__":
    result = even_fib(25)
    print(f"The sum of the even-valued terms in the Fibonacci sequence not exceeding four million is: {result}")