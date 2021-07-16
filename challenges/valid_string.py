"""
## Valid Strings

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

**Explanation**
- Use a stack (first in last out approach) to keep track of opening characters
"""

def valid_string(string):
    mapping = {')':'(',']':'[','}':'{'}
    stack = []
    
    for s in string:
        if s in mapping and mapping[s] in stack:
            stack.remove(mapping[s])
        else:
            stack.append(s)
    if stack:
        return False
    else: 
        return True
        
string = '([{}])'
valid_string(string)