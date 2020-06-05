def fibonacci(n):
    """fibonacci series function 0, 1, 1, 2, 3, 5, 8, 13, ..."""
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return (fibonacci(n-1) + fibonacci(n-2))
print(fibonacci(7))


def lucas(n):
    """lucas number series function 2, 1, 3, 4, 7, 11, 18, 29, ..."""
    if n == 0:
        return 2
    if n == 1:
        return 1
    if n == 2:
        return 3
    else:
        return (lucas(n-1) + lucas(n-2))
print(lucas(7))


def sum_series(n, first=0, second=1):
    """sum series with one required parameter and two optional parameters.""" 
    if n == 0:
        return first
    elif n == 1:
        return second 
    else:
        return(sum_series(n-1, first, second) + sum_series(n-2, first, second))
print(sum_series(3,6,6))

