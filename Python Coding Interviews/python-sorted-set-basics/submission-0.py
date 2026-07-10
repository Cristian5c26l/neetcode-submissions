from typing import List
from sortedcontainers import SortedSet


def get_first_three(sorted_set: SortedSet[int], nums1: List[int], nums2: List[int]) -> List[int]:
    
    for n in nums1:
        sorted_set.add(n)

    
    for n in nums2:
        sorted_set.discard(n)# It's possible some elements in nums2 may not exist in the sorted set, so ensure your code does not raise an error in this case.

    res = []

    for n in sorted_set:
        if len(res) == 3:
            break
        res.append(n)

    return res


# do not modify below this line
print(get_first_three(SortedSet(), [1, 2, 3], [4]))
print(get_first_three(SortedSet([1, 4, 7, 2, 8, 9]), [10], [1, 7, 2]))
print(get_first_three(SortedSet([1, 2, 3, 7]), [], [4, 5, 6]))
print(get_first_three(SortedSet([1, 2, 3, 4, 5, 6, 7, 8, 9]), [10, 11, 12], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
