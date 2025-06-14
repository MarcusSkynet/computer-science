# Global cache for memoization
memo = {}

def fibonacci(num):
    """
    Return the nth Fibonacci number using recursion with memoization.

    Parameters
    ----------
    num : int
        The index (n) of the Fibonacci sequence to retrieve. Must be non-negative.

    Returns
    -------
    int
        The nth Fibonacci number.

    Raises
    ------
    TypeError
        If num is not an integer.
    ValueError
        If num is negative.
    """
    # 1. Validate input type
    if not isinstance(num, int):
        raise TypeError(f"Expected integer, got {type(num).__name__}")
    # 2. Handle negatives explicitly
    if num < 0:
        raise ValueError("Fibonacci number is not defined for negative integers")

    # 3. Check memoization cache
    if num in memo:
        return memo[num]

    # 4. Base cases
    if num == 0:
        result = 0
    elif num == 1:
        result = 1
    else:
        # 5. Recursive computation
        result = fibonacci(num - 1) + fibonacci(num - 2)

    # 6. Store in cache
    memo[num] = result
    return result

def fibonacci_iter(n):
    if not isinstance(n, int):
        raise TypeError(f"Expected integer, got {type(n).__name__}")
    if n < 0:
        raise ValueError("Fibonacci number is not defined for negative integers")
    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b


# Example usage:
if __name__ == "__main__":
    # This will print:
    # fibonacci(20): 6765
    # fibonacci(200): 280571172992510140037611932413038677189525
    print("fibonacci(20):", fibonacci(20))
    print("fibonacci(200):", fibonacci(200))
