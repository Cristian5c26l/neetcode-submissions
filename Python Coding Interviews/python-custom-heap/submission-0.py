import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    max_heap = []

    for n in nums:
        pair = (-n, n)
        heapq.heappush(max_heap, pair)# It's still a min heap where the top is the smallest priority located in each pair[0] of the heap

    result = []

    while max_heap:
        pair = heapq.heappop(max_heap)
        _, original_num = pair
        result.append(original_num)

    return result



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
