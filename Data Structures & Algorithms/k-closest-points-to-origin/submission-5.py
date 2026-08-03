from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # New Base Case on quick_sort: if s == 0 and e - s + 1 >= k

        def quick_sort(points, s, e, k):

            #if e == k - 1:
            #    return list(set(points[0:k]))
            
            if e - s + 1 <= 1:
                return points

            pivot = points[e]
            left = s# pointer a
            building_k = s

            for i in range(s, e):# i is pointer b
                x2, y2 = points[i][0], points[i][1] 
                if sqrt(((0 - x2) ** 2) + ((0 - y2) ** 2)) < sqrt(((0 - pivot[0]) ** 2) + ((0 - pivot[1]) ** 2)):
                    points[i], points[left] = points[left], points[i]
                    left += 1
                    building_k += 1

            # i has reached e
            points[left], points[e] = pivot, points[left]
            building_k += 1

            # At this point, before the pivot value are smaller values (likely unsorted), and after are greater values (likely unsorted). Moreover, pivot is already sorted.

            print("points: ", points)
            print("left: ", left)
            print("k: ", k)

            if building_k == k or left == k:
                return points[0:k]

            if left + 1 < k: 
                return quick_sort(points, left + 1, e, k)
            elif left + 1 > k:
                return quick_sort(points, s, left - 1, k)


        return quick_sort(points, 0, len(points) - 1, k)
        