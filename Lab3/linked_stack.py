from abstract_stack import Stack
from node import Node


class LinkedStack(Stack):
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped = self.top.data
            self.top = self.top.next
            return popped
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            print("Stack is empty")

    def is_empty(self):
        return self.top is None

    def is_full(self):
        # LinkedStack doesn't have a max size
        return False
