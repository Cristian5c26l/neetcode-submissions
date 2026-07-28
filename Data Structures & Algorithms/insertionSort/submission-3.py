# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # Relative Order (stable): Order which items already are in pairs input
        if len(pairs) == 0:
            return []

        # Suppose pairs input = [(5, "..."), (2, "..."), (1, "...")]
        insertion_sort_states = [pairs[:]]# cloned_list_pairs = copy.deepcopy(pairs) = pairs[:]

        #i = 1# Due to 5 is a portion ordered, we start at pairs[1] (2) to order the portion 5,2

        # Cormen approach
        # Initialization
        for i in range(1, len(pairs)):# 1 to 2 
            
            # Maintenance
            pair_key = pairs[i]# pair_key represents the element to insert
            j = i - 1# Due to 5 is a portion ordered (pairs[0:0]), we start at pairs[1] (j = 1 which stores 2) to order de portion 5,2.

            while j >= 0 and pairs[j].key > pair_key.key:
                pairs[j + 1] = pairs[j]
                j -= 1

            pairs[j + 1] = pair_key 
            insertion_sort_states.append(pairs[:])

        # Termination
        # Initialization, Maintenance and Termination are the steps of the loop invariant method to prove thar insertion sort algorithm is correct. To make that provement, it is necesarry find the loop invariant of insertion sort. The loop invariant (property that always has to met) of insertion sort is that the subarray pairs[0:i-1] is ordered and contain the same elements which are expected.

        return insertion_sort_states



        