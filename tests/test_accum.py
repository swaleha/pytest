"""
This module contains basic unit tests for accum module.
The purpose is to show the usage of pytest framework with example.
3 step pattern to write functional test cases

Arrange: arrange assets for the test
Act: act by exercising the target behavior
Assert: assert that expected outcomes happen
"""

#----------------------------------------------------
# Imports
#----------------------------------------------------

import pytest
from stuff.accum import Accumulator

#----------------------------------------------------
# Fixtures: paramter 'accum' i.e object of Accumulator 
# class comes from the fixture present in conftest.py file
#----------------------------------------------------
@pytest.fixture
def accum():
    return Accumulator()

#----------------------------------------------------
# Tests
#----------------------------------------------------

def test_accumulator_init(accum):
    assert accum.count == 0
    
def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1
    
def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3
    
def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2
    
def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match =r"can't set attribute") as e:
        accum.count = 10
