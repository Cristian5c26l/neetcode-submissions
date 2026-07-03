from typing import List

"""
Time Complexity

index():

Time complexity: O(n) where n is the length of the list.

remove():

Time complexity: O(n) where n is the length of the list.

extend():

Time complexity: O(m) where m is the length of the list passed to extend().

in operator on a list:

Time complexity: O(n) where n is the length of the list.
"""

def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    arr1.extend(arr2)
    return arr1
  

def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    
    for num in arr2:
        if num in arr1:
            arr1.remove(num)

    return arr1


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))
