from typing import List, Any
import operator

def all_the_same(elements: List[Any]) -> bool:
    # your code here
    if len(elements) > 0:
        count = 0
        values = {}
        for i in elements:
            if i in values:
                values[i] += count+1
            else:
                values[i] = count+1
        
        maxValKey = max(values, key=values.get)
        maxVal = values[maxValKey]

        if maxVal == len(elements):
            return True
        else:
            return False
    else:   
        return True


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))
    
    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")