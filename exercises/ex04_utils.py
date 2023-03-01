"""EX04 - utils """

__author__ = "730476529"

def all(integers: list[str],find: int )-> bool:
    """checks if all number in the list of integers matches the find integer"""
    i=0
    if len(integers) == 0:
        return False 
    while i < len(integers):
        if integers[i]!= find:
            return False 
        i+= 1
    return True 

def max(input: list[int]) -> int:
    """returns maximum number out of a list of numbers"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        i=0
        maximum: int = input[i]
        while i < len(input):
            if maximum < input[i]:
                maximum = input[i]
            i+= 1
        return maximum
    
def is_equal(list1: list[int], list2: list[int])-> bool:
    """states if string one matches string 2"""
    i: int= 0
    if len(list1) == 0 and len(list2) == 0:
        return True
    if len(list1) != len(list2):
        return False
    while i < len(list2):
        if list1[i]!= list2[i]:
            return False
        i+=1
    return True