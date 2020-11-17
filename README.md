## Problem Statement
* Build a calculator package that has separate module for:
    * sin, cos, tan, tanh, SoftMax, Sigmoid, ReLU, log and e
    * The modules shall include their derivatives as well
    * If we do import calculator, we should be able to access all the above function (except deviratives)
    * For derivates we must do: from package import derivatives. 
    * Outputs are returned as well as printed using only f-string
    * Write simple test cases to check the outputs of each operator and their derivative

## Solution
We create a `calculator` package which implements functions `{sin, cos, tan, tanh, softmax, sigmoid, relu, log, exp}`. In order to export derivatives seperately, we use `__all__` in our `__init__` file to let python know which functions should load when we `import calculator`. 

### Derivatives
`derivatives.py` imports all the derivative functions from each module in `calculator` package. We include all the functions in `__all__`. 

### Tests
More than 20 tests one for each function and its derivative are implemented.



