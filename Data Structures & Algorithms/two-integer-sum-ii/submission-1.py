class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Time Complexity: O(n)

        # Pattern: Two Pointers

        L, R = 0, len(numbers) - 1# index1, index2. Both of them cannot be equal

        res = [0,0]
        while L < R:
            if numbers[L] + numbers[R] > target:
                R -= 1
            elif numbers[L] + numbers[R] < target:
                L += 1
            else:
                res[0], res[1] = L + 1, R + 1
                break

        return res

        