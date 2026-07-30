class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def mergee(nums1, s, m, e):
            L = nums1[s: m + 1]
            R = nums1[m + 1: e + 1]

            i = 0
            j = 0
            k = s

            # Merge the two sorted halfs L and R
            while i < len(L) and j < len(R):# Modifying nums1 in-place 
                if L[i] <= R[j]:
                    nums1[k] = L[i]
                    i += 1
                else:
                    nums1[k] = R[j]
                    j += 1

                k += 1

            while i < len(L):
                nums1[k] = L[i]
                k += 1
                i += 1

            while j < len(R):
                nums1[k] = R[j]
                k += 1
                j += 1

        def merge_sort(nums1, s, e):
            if e - s + 1 <= 1:
                return

            m = (s + e) // 2

            merge_sort(nums1, s, m)
            merge_sort(nums1, m + 1, e)

            mergee(nums1, s, m, e)

        nums1[m:] = nums2[:n]
        # Time Complexity: O((m + n)log(m + n))
        # Space Complexity: O(m + n)
        merge_sort(nums1, 0, len(nums1) - 1)
        