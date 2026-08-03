class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def quick_select(points, s, e, k):

            #if e == k - 1:
            #    return list(set(points[0:k]))
            
            if s >= e:# No more partition/selection
                return points[:k]

            pivot = points[e]
            left = s# pointer a

            for i in range(s, e):# i is pointer b
                x2, y2 = points[i][0], points[i][1] 
                if (x2 ** 2) + (y2 ** 2) < (pivot[0] ** 2) + (pivot[1] ** 2):
                    points[i], points[left] = points[left], points[i]
                    left += 1
            

            # i has reached e
            points[left], points[e] = pivot, points[left]

            # At this point, before the pivot value (points[left]) are smaller values (likely unsorted), and after are greater values (likely unsorted). Moreover, pivot is already sorted.

            if left == k - 1:
                return points[:k]

            # Quick select
            if left < k - 1: 
                return quick_select(points, left + 1, e, k)
            else:# left > k -1:
                return quick_select(points, s, left - 1, k)


        return quick_select(points, 0, len(points) - 1, k)
        