from typing import List

"""
Time complexity: O(n) where n is the length of the list being copied.
"""

def remove_element(arr: List[int], element: int) -> List[int]:
    cloned_arr = arr.copy()
    cloned_arr.remove(element)
    return cloned_arr



# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)
