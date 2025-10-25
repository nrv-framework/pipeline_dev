def collatz(n: int):
    """ computes the next number in the Collatz sequence
    Args:
        n (int): A positive integer    
    Returns:
            int: The next number in the Collatz sequence
    Raises:
        ValueError: If n is not a positive integer
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    while n != 1:
        if n//2 == 0:
            return n/2
        else:
            return 3*n + 1

    