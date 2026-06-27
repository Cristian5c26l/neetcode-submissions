class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #times = [0] * len(position)

        # Optimal solution
        # Time complexity: O(nlogn)
        # Space complexity: O(n)

        pos_speed_dict = dict(zip(position, speed))

        list_pos_speed_sorted = sorted(pos_speed_dict.items(), reverse=True)# O(nlogn) Sorted desc by position: [(position, speed)] [(4,2), (2,1), (1,1)]

        times = []
        for p, s in list_pos_speed_sorted:#O(n)
            times.append((target - p) / s)

        stack = []

        for time in times:#O(n)
            if len(stack) == 0 or time > stack[-1]:# stack is empty or the time of car B (time) is greater than the time of car B (stack[-1]) to arrive to the target, there is a new car fleet.
                stack.append(time)

        return len(stack)
        