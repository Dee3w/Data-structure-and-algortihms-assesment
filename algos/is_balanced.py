def is_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in brackets.values():  # Opening bracket
            stack.append(char)
        elif char in brackets.keys():  # Closing bracket
            if not stack or stack.pop() != brackets[char]:
                return False
    
    return not stack  # If the stack is empty, the expression is balanced

# Test cases
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False
