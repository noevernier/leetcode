from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for e in tokens:
            if e=="+":
                left_operand = int(stack.pop())
                right_operand = int(stack.pop())
                stack.append(str(left_operand+right_operand))
            elif e=="-":
                left_operand = int(stack.pop())
                right_operand = int(stack.pop())
                stack.append(str(left_operand-right_operand))
            elif e=="*":
                left_operand = int(stack.pop())
                right_operand = int(stack.pop())
                stack.append(str(left_operand*right_operand))
            elif e=="/":
                left_operand = int(stack.pop())
                right_operand = int(stack.pop())
                stack.append(str(left_operand/right_operand))
            else:
                stack.append(e)
