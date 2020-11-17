
import pytest
import re
import inspect
import os
import math
from calculator import *
from calculator import derivatives

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
    assert len(readme_words) >= 300, "Make your README.md file interesting! Add atleast 500 words"

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