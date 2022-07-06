"""
This module contains basic unit tests for math operations.
The purpose is to show usage of pytest framework by example
"""
#----------------------------------------------------
# Imports
#---------------------------------------------------- 

import pytest

#----------------------------------------------------
# The most basic test function
#----------------------------------------------------

@pytest.mark.math
def test_one_plus_one():
    assert 1 + 1 == 2
    
    
#----------------------------------------------------
# A test function to show assertion introspection
#----------------------------------------------------

@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3    # c = 0 
    assert a + b == c
   
   
#----------------------------------------------------
# A test function that verifies the exception
#---------------------------------------------------- 

@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    
    assert 'division by zero' in str(e.value)

#----------------------------------------------------
# A test function that shows parameterized test function
#---------------------------------------------------- 

# multiplication test ideas: Equivalence classes for test case inputs 


products = [
    (2, 3, 6),        # two positive numbers
    (1, 99, 99),      # Identity
    (0, 100, 0),      # zero
    (3, -4, -12),     # positive by negative
    (-5, -5, 25),     # negative by a negative
    (2.5, 6.7, 16.75) # floating point numbers
 
]

@pytest.mark.math
@pytest.mark.parametrize('a, b, product', products) 
def test_multiplication(a, b, product):
    assert a * b == product

