import math

def tanh(theta):
    '''
       function to calculate tanh of an angle in radians
       Args:
           theta: angle in degrees
       Returns: tanh theta value
       '''
    print(f'tanh value : {math.tanh(theta)}')
    return math.tanh(theta)

def dtanh(theta):
    '''
       function to calculate derivative of tanh
       Args:
           theta: angle in degrees
       Returns: derivative of tanh
       '''
    print(f'derivative of tanh : {1 - math.tanh(theta)**2}')
    return (1 - math.tanh(theta)**2)