from abstract_stack import Stack

class DictStack(Stack):
    def __init__(self):
        self.stack = {}

    def push(self, key, value):
        if key in self.stack:
            print("Key already exists in the stack")
        else:
            self.stack[key] = value

    def pop(self):
        if not self.is_empty():
            key, value = self.stack.popitem()
            return key, value
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            key, value = next(reversed(self.stack.items()))
            return key, value
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return False
