import math
from math import sin, cos, radians

def cos_(theta):
    '''
       function to calculate cos of an angle in radians
       Args:
           theta: angle in degrees
       Returns: cos theta value
       '''
    print(f'cos theta : {math.cos(radians(theta))}')
    return cos(radians(theta))

def dcos(theta):
    '''
       function to calculate derivative of cos
       Args:
           theta: angle in degrees
       Returns: cos derivative value
       '''
    
    return_value = sin(radians(theta))
    if return_value == 0:
        print(f'derivative of cos theta : {return_value}')
        return return_value
    else:
        print(f'derivative of cos theta : {-return_value}')
        return -return_value