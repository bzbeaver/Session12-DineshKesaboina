# imports
from math import tan, radians
import mpmath

def tan_(theta):
    '''
       function to calculate tan of an angle in radians
       Args:
           theta: angle in degrees
       Returns: tan theta value
       '''
    print(f'tan theta : {tan(radians(theta))}')
    return tan(radians(theta))

def dtan(theta):
    '''
       function to calculate derivative of tan
       Args:
           theta: angle in degrees
       Returns: derivative of tan
       '''
    print(f'derivative of tan theta :{mpmath.sec(mpmath.radians(theta))**2}')
    return mpmath.sec(mpmath.radians(theta)**2)
