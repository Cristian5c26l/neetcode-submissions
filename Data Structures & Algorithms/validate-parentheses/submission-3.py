class Solution:
    def isValid(self, s: str) -> bool:

        # Optimal Solution
        # Time complexity: O(n)
        # Space complexity: O(n) (due to having for example the "(({{[" string)

        stack = []# Stack is an implementation of dynamic array
        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            elif char in [')', '}', ']'] and len(stack):# len has O(1) of time complexity
                top = stack[-1]
                if char == ')' and top == '(':
                    stack.pop()
                elif char == '}' and top == '{':
                    stack.pop()
                elif char == ']' and top == '[':
                    stack.pop()
                else:
                    return False
            else:
                return False

        return len(stack) == 0
