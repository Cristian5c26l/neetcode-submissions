from typing import List

"""
Time complexity: O(n + m) where n is the length of one list and m is the length of the other list.
"""

def combine_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    return arr1 + arr2



# do not modify below this line
arr1 = [1, 3, 5]
arr2 = [4, 6, 8]

print(combine_elements(arr1, arr2))
print(arr1)
print(arr2)
