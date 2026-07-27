# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

import copy

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # Relative Order (stable): Order which items already are in pairs input
        if len(pairs) == 0:
            return []

        # Suppose pairs input = [(5, "..."), (7, "..."), (4, "...")]
        insertion_sort_states = [copy.deepcopy(pairs)]# cloned_list_pairs = copy.deepcopy(pairs)

        #i = 1# Due to 5 is a portion ordered, we start at pairs[1] (7) to order de portion 5,7

        for i in range(len(pairs) - 1):# 0 to (3 - 1), thus 0 to 1
            
            j = i + 1# Due to 5 is a portion ordered, we start at pairs[1] (j = 1 which stores 7) to order de portion 5,7. First i = 0, j = 1; and then i = 1, j = 2

            while j > 0 and pairs[j].key < pairs [j - 1].key:# while j > 0 and current one < before one
                greater = pairs[j - 1]
                pairs [j - 1] = pairs[j]
                pairs[j] = greater
                j -= 1

            insertion_sort_states.append(copy.deepcopy(pairs))

        return insertion_sort_states



        