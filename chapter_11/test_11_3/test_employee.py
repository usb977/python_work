import pytest
from employee import Employee

@pytest.fixture
def test_person():
    person = Employee('Dylan','Jack',8000)
    return person

def test_give_default_raise(test_person):
    """测试默认增加值"""
    money = test_person.give_raise()
    assert money == 13000

def test_give_custom_raise(test_person):
    """测试默认增加值"""
    money = test_person.give_raise(8000)
    assert money == 16000