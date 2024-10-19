

def caching_fibonacci():

    """
    Returns a function that calculates Fibonacci numbers using memoization (caching). 
    This helps to avoid recalculating the same values multiple times and makes the function faster.

    The returned function `fibonacci(n)` will calculate the nth Fibonacci number.
    It uses a dictionary (cache) to store results of previous calculations and reuses them 
    to avoid doing the same work again.

    Returns:
        function: a function `fibonacci(n)` that takes an integer n and returns the nth Fibonacci number.

    
    Parameters:
        n (int): the position in the Fibonacci sequence to calculate. Should be a non-negative integer.

    """

    cache = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return n
        
        if n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    
    return fibonacci

# Get the fibonacci function
fib = caching_fibonacci()

# Use the fibonacci function to calculate Fibonacci numbers
print(fib(10)) # Outputs 55
print(fib(15)) # Outputs 610

