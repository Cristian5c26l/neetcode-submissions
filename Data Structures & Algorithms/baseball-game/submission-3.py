class Solution:
    def calPoints(self, operations: List[str]) -> int:

        # Optimal solucion
        # Time complexity: O(n)
        # Space Complexity: O(n) (due to the worst case of having an operations array with only numbers which leads to an stack of size n)

        scores_stack = []
        stack_top = None
        points = 0
        for operation in operations:# O(n)
            if operation not in ["C", "D", "+"]:# O(1): Push (append)
                scores_stack.append(int(operation))
                stack_top = scores_stack[-1]
                points += stack_top 
                continue
            
            if operation == "+":
                new_score = stack_top + scores_stack[-2]
                scores_stack.append(new_score)
                points += new_score
            elif operation == 'D':
                new_score = 2 * stack_top
                scores_stack.append(new_score)
                points += new_score
            elif operation == 'C':# O(1): Pop
                deleted_score = scores_stack.pop()
                points -= deleted_score

            stack_top = scores_stack[-1] if len(scores_stack) > 0 else None 

        return points