from collections import deque

def isValid(s : str):
    stack = []
    brackets_map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    for p in s:
        if p in brackets_map:
            stack.append(p)
        elif stack and brackets_map[stack[-1]] == p:
            stack.pop()
        else:
            return False
    
    return not stack

print(isValid("(){[]"))