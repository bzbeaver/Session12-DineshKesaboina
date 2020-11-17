import math

def sigmoid(somenum):
    '''
       function to calculate sigmoid of a number

       Args:
           somenum: int or float

       Returns: sigmoid of a number
       '''

    print(f'Sigmoid of {somenum} is {(1 / (1 + math.exp(-somenum)))}')
    return (1 / (1 + math.exp(-somenum)))

def dsigmoid(somenum):
    """function to calculate the derivative of sigmoid of a number

    Args:
        somenum ([int or float]): somenum for which derivative of sigmoid need to be calculated.

    Returns:
        float: derivative of sigmoid of some number
    """
    print(f'Derivative of sigmoid for {somenum} is {sigmoid(somenum) * (1 - sigmoid(somenum))}')
    return sigmoid(somenum) * (1 - sigmoid(somenum))

# Reference : https://towardsdatascience.com/derivative-of-the-sigmoid-function-536880cf918e