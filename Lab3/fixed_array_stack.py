from abstract_stack import Stack


class FixedArrayStack(Stack):
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [None] * max_size
        self.top = -1

    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.stack[self.top] = item
        else:
            print("Stack is full")

    def pop(self):
        if not self.is_empty():
            popped = self.stack[self.top]
            self.top -= 1
            return popped
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.stack[self.top]
        else:
            print("Stack is empty")

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1
