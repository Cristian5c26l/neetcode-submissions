from typing import List

"""
Time Complexity

append():

Time complexity: O(1)

pop():

Time complexity: O(1)

insert():

Time complexity: O(n), where n is the number of elements in the list.


"""

def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for num in arr2:
        arr1.append(num)
    
    return arr1



def pop_n(arr: List[int], n: int) -> List[int]:
    count = 0
    while len(arr) > 0 and count < n:
        arr.pop()
        count += 1

    return arr


def insert_at(arr: List[int], index: int, element: int) -> List[int]:
    if 0 <= index <= len(arr) - 1:
        arr.insert(index, element)
    else:# Out of bounds
        arr.append(element)

    return arr


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(pop_n([1, 2, 3, 4, 5], 2))
print(pop_n([1, 2, 3, 4, 5], 6))
print(pop_n([1, 2, 3, 4, 5], 5))

print(insert_at([1, 2, 3, 4, 5], 2, 6))
print(insert_at([1, 2, 3, 4], 6, 5))
