def factorial(n):
    """
    Calculate the factorial of a given number.

    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the given number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the factorial function
if __name__ == "__main__":
    num = 5
    print(f"The factorial of {num} is {factorial(num)}")
