class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #times = [0] * len(position)

        pos_speed_dict = dict(zip(position, speed))

        list_pos_speed_sorted = sorted(pos_speed_dict.items(), reverse=True)# Sorted desc by position: [(position, speed), (), ()]

        times = []
        for p, s in list_pos_speed_sorted:
            times.append((target - p) / s)

        stack = []

        for time in times:
            if len(stack) == 0 or time > stack[-1]:
                stack.append(time)

        return len(stack)
        