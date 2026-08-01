# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        def quick_sort(pairs, s, e):
            if e - s + 1 <= 1:
                return pairs
            
            pivot = pairs[e]
            left = s # pointer a 

            for i in range(s, e):# i is pointer b
                if pairs[i].key < pivot.key:
                    pairs[left], pairs[i] = pairs[i], pairs[left]# swap
                    left += 1

            # i has reached e at this point
            pairs[left], pairs[e] = pivot, pairs[left]

            quick_sort(pairs, s, left - 1)
            quick_sort(pairs, left + 1, e)

            return pairs

        s = 0
        e = len(pairs) - 1

        return quick_sort(pairs, s, e)