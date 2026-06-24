class Solution:
    def calPoints(self, operations: List[str]) -> int:

        # Optimal solucion
        # Time complexity: O(n)
        # Space Complexity: O(n) (due to the worst case of having an operations array with only numbers which leads to an stack of size n)

        scores_stack, points = [], 0
        for operation in operations:# O(n)
            if operation not in ["C", "D", "+"]:# O(1): Push (append)
                scores_stack.append(int(operation))
                points += scores_stack[-1]# scores_stack[-1] is the top
                continue
            
            if operation == "+":
                new_score = scores_stack[-1] + scores_stack[-2]
                scores_stack.append(new_score)
                points += new_score
            elif operation == 'D':
                new_score = 2 * scores_stack[-1]
                scores_stack.append(new_score)
                points += new_score
            elif operation == 'C':# O(1): Pop
                deleted_score = scores_stack.pop()
                points -= deleted_score 

        return points