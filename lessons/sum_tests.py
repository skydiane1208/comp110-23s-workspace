"""Unit tests for sum function"""

from lessons.sum import sum 

def test_empy() -> None:
    assert sum([]) == 0.0
    
def test_one_element() -> None:
    test_list: list[float] = [1.0]
    assert sum(test_list) == 1.0
    
def test_many() -> None:
    test_list: list[float] = [1.0, 2.0, 3.0]
    assert sum(test_list) == 0.0
    
def test_many_with_negative() -> None:
    test_list: list[float] = [1.0, -2.0, 1.0]
    assert sum(test_list) == 0.0
    
    