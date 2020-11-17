import math

def log(somenum):
    '''
       function to calculate log of a number
       Args:
           arg: argument is in numeric
       Returns: log value of a number
       '''
    print(f'Log of {somenum} is {math.log(somenum)}')
    return math.log(somenum)

def dlog(somenum):
    '''
       function to calculate derivative of log of a number
       Args:
           arg: argument is in numeric
       Returns: derivative of log of a number
       '''
    if isinstance(somenum, int) or isinstance(somenum, float):
        if somenum == 0:
            print("Log of 0 is undefined")
        else:
            print(f"Derivative is {1/somenum}")
        return ((1 / somenum) if somenum!=0 else "Log of 0 : undefined")