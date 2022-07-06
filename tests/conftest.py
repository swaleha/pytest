#----------------------------------------------------
# Fixtures: fixtures will run only once by default
# when the function needs it. 
#----------------------------------------------------
"""
import pytest
@pytest.fixture
def accum():
    return Accumulator()
"""


# Replacing return statement from the fixture makes it a generator. 
# After the fixture's yield statement will be the clean up steps
"""
@pytest.fixture
def accum():
    yield Accumulator()
    print("Done!")
"""