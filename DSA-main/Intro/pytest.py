'''
Pytest: Python testing made easy
Popular testing framework for Python. Simple, powerful, and support features like fixtures, parameterized tests and detailed failure reports.
Works with existing unittest or nose tests.
Auto-discovery of tests in files named test.*.py or *_test.py

pip install pytest
pip install pytest-django

Fixtures helps us test data or state

@pytest.mark.parametrize is Pytest decorator that lets run same test function multiple times with different values
'''

def add(a, b):
    return a+b 

def test_add():
    assert add(2, 3)==5

import pytest 
@pytest.fixture
def sample_user():
    return {"name": "Alice", "age":30}

def test_user_name(sample_user):
    assert sample_user["name"]=="Alice"

@pytest.mark.parametrize("a, b, expected", [
    (1,2,3),
    (5,5,10),
    (-1,1,0)
])
def test_add(a,b,expected):
    assert a+b==expected

