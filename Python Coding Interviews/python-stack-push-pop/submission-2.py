from typing import List

"""
Time Complexity

1. append(): O(1)

2. pop(): O(1)

3. [-1]: O(1)

4. len(): O(1)

"""

def reverse_list(arr: List[int]) -> List[int]:
    
    new_list = []
    while len(arr) > 0:
        new_list.append(arr.pop())

    return new_list
    


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
