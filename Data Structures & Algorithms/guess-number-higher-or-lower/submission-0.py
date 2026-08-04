# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        # O(logn)
        low, high = 1, n  
        picked_n = low# picked number in guess function
        while low <= high:
            guess_n = (low + high) // 2# guess_n is a mid number inside of the low-high range

            if guess(guess_n) > 0:# == 1, i.e, if guess_n is lower than the number
                low = guess_n + 1
            elif guess(guess_n) < 0: # == -1:
                high = guess_n - 1
            else:# guess(guess_n) == 0:
                picked_n = guess_n
                break

        return picked_n


        