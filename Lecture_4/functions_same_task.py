def bisection_cuberoot(x, epsilon):
    '''
    Input: x, an integer
    Uses bisection to approximate the cube root of x to within epsilon
    Returns: a float approximating the cube root of x
    '''
    low = 0.0
    high = x