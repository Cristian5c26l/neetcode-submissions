from typing import List, Deque
from collections import deque

"""
Time Complexity

appendleft(): O(1)

pop(): O(1)
"""

def rotate_list(arr: List[int], k: int) -> Deque[int]:
    queue = deque()
    for element in arr:
        queue.append(element)

    rotation = 0
    while rotation < k:
        queue.appendleft(queue.pop())
        rotation += 1
    
    return queue


# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))
