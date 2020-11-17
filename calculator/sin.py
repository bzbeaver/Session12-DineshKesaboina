import math
from math import sin, cos, radians


def sin_(theta):
    '''
       function to calculate sin of an angle in radians
       Args:
           theta: angle in degrees
       Returns: sin theta value
       '''
    print(f'sin theta : {math.sin(radians(theta))}')
    return sin(radians(theta))

def dsin(theta):
    '''
       function to calculate derivative of sin
       Args:
           theta: angle in degrees
       Returns: sin derivative value
       '''
    print(f'derivative of sin theta :{cos(radians(theta))}')
    return cos(radians(theta))