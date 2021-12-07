"""
Create a Stack Data Structure
LIFO: Last In First Out

Methods:
push: pushes item onto the stack
pop: removes last item from the stack

NOTE: all push/pop operations are taken at the top of the stack.
"""


class Stack:
    def __ini__(self):
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        """pop element from stack"""
        if len(self.stack) > 0:
            return self.stack.pop()


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.pop()
    print(s)
