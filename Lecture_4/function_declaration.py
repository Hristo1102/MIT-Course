def is_even_with_return( i ):
    """
    Input: i, a positive int
    Returns True if i is even, otherwise False
    """
    remainder = i % 2
    return remainder == 0

print(is_even_with_return(3))