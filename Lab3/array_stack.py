from abstract_stack import Stack


class ArrayStack(Stack):
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = []

    def push(self, item):
        if not self.is_full():
            self.stack.append(item)
        else:
            print("Stack is full")

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty")

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.max_size
