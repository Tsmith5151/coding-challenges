def isValidSerialization(preorder):
    preorder, stack = preorder.split(","), []
    for node in preorder:
        print(stack)
        while stack and node == stack[-1] == "#":
            stack.pop()
            if not stack:
                return False
            stack.pop()
        stack.append(node)
    return stack == ["#"]


def dailyTemperatures(T):
    """ Compute Temperatures using Stacks """
    delta = [0] * len(T)
    stack = []
    for i in range(0,len(T)):
        while stack and T[i] > T[stack[-1]]:
            idx = stack.pop()
            delta[idx] = i - idx
        stack.append(i)
    return delta
