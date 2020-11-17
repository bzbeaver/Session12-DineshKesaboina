def relu(x):
    """[summary]

    Args:
        x (numeric): some number
    Returns:
        numeric : max of zero and input number
    """

    print(f'Relu of {x} is: {max(0, x)}')
    return max(0, x)

def drelu(x):
    """Computes relu derivative of the given input"""

    print(f'Derivative of Relu for {x} is: {1 if x > 0 else 0}')
    return 1 if (x > 0) else 0
