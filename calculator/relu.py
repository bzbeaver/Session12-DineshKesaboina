def relu(x):
    """[summary]

    Args:
        x ([type]): [description]

    Raises:
        TypeError: [description]

    Returns:
        [type]: [description]
    """
    if not isinstance(x, int) or not isinstance(x, float):
        raise TypeError("Enter a valid number type")

    print(f'Relu of {x} is: {max(0, x)}')
    return max(0, x)

def drelu(x):
    """Computes relu derivative of the given input"""
    if not isinstance(x, int) or not isinstance(x, float):
        raise TypeError("Enter a valid number type")

    print(f'Derivative of Relu for {x} is: {1 if x > 0 else 0}')
    return 1 if (x > 0) else 0
