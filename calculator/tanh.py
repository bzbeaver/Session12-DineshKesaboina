import math

def tanh(theta):
    '''
       function to calculate tanh of an angle in radians
       Args:
           theta: angle in degrees
       Returns: tanh theta value
       '''
    print(f'tanh value : {math.tanh(math.radians(theta))}')
    return math.tanh(math.radians(theta))

def dtanh(theta):
    '''
       function to calculate derivative of tanh
       Args:
           theta: angle in degrees
       Returns: derivative of tanh
       '''
    print(f'derivative of tanh : {1 - math.tanh(math.radians(theta))**2}')
    return (1 - math.tanh(math.radians(theta))**2)