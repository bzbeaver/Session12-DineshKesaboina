
import numpy as np

def softmax(some_array):
    '''function to calculate softmax

       Args:
           some_array ([list or tuple]): some array which is a numeric vector

       Returns: array of softmax value
       '''
    assert len(some_array) > 1, 'Array should have atleast 2 elements'


    print(f'{np.exp(some_array) / np.sum(np.exp(some_array))}')
    return np.exp(some_array) / np.sum(np.exp(some_array))

def dsoftmax(some_array):
    """function to calculate the derivative of softmax

    Args:
        some_array ([list or tuple]): some array which is a numeric vector

    Returns:
        list or tuple: array of softmax value
    """
    softmax_output = softmax(some_array)
    softmax_output = np.reshape(softmax_output, (1, -1))
    d_softmax = (softmax_output * np.identity(softmax_output.size) - softmax_output.transpose() @ softmax_output)
    print(f'Derivative of softmax is: {d_softmax}')
    return d_softmax

# Reference : https://e2eml.school/softmax.html