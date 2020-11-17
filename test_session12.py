
import pytest
import re
import inspect
import os
import math
import calculator
from calculator import derivatives
import numpy as np

README_CONTENT_CHECK_FOR = [
                'calculator',
                'module',
                'package',
                'cos',
                'sin',
                'log',
                'relu',
                'sigmoid',
                'softmax',
                'tan',
                'tanh',
                'derivatives',
                'exp',
                '__init__',
                '__all__',
                'import',
            ]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 150, "Make your README.md file interesting! Add atleast 150 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10
    
def test_sin_():
    assert calculator.sin_(0) == 0.0
    
def test_dsin_without_from():
    with pytest.raises(AttributeError):
        calculator.dsin(0)

def test_dsin():
    from calculator import derivatives
    assert derivatives.dsin(30) == 0.8660254037844387
    
def test_cos_():
    assert calculator.cos_(0) == 1.0
    
def test_dcos_without_from():
    with pytest.raises(AttributeError):
        calculator.dcos(0)
        
def test_dcos():
    from calculator import derivatives
    assert derivatives.dcos(30) == -0.49999999999999994
    
def test_tan():
    assert calculator.tan_(45) == 0.9999999999999999
    
def test_tanh():
    assert calculator.tanh(30) == 0.48047277815645156
    
def test_dtanh_without_from():
    with pytest.raises(AttributeError):
        calculator.dtanh(0)

def test_dtanh():
    from calculator import derivatives
    assert derivatives.dtanh(30) == 0.7691459094506212

def test_softmax():
    assert calculator.softmax([3,4,5])[2] == 0.6652409557748219
    assert calculator.softmax([3,4,5])[1] == 0.24472847105479764
    assert calculator.softmax([3,4,5])[0] == 0.09003057317038046

def test_softmax_without_from():
    with pytest.raises(AttributeError):
        calculator.dsoftmax([3,4,5])

def test_dsoftmax():
    from calculator import derivatives
    return_ = derivatives.dsoftmax([3,4,5])
    assert return_[0][0] == 0.08192506906499324
    assert return_[0][1] == -0.022033044520174298
    assert return_[0][2] == -0.059892024544818935

def test_sigmoid():
    assert calculator.sigmoid(0) == 0.5
    
def test_dsigmoid_without_from():
    with pytest.raises(AttributeError):
        calculator.dsigmoid(0)

def test_dsigmoid():
    assert derivatives.dsigmoid(0) == 0.25
    
def test_relu():
    assert calculator.relu(5) == 5

def test_drelu_without_from():
    with pytest.raises(AttributeError):
        calculator.drelu(5)

def test_drelu():
    assert derivatives.drelu(5) == 1

def test_log():
    assert calculator.log(1) == 0.0

def test_dlog_without_from():
    with pytest.raises(AttributeError):
        calculator.dlog(5)

def test_dlog():
    assert derivatives.dlog(5) == 0.2
    
def test_exp():
    assert calculator.exp(5) == 148.4131591025766

def test_dexp_without_from():
    with pytest.raises(AttributeError):
        calculator.dexp(5)
        
def test_dlog():
    assert derivatives.dexp(5) == 148.4131591025766

