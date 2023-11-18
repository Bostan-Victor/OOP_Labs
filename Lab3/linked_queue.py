from abstract_queue import Queue
from node import Node


class LinkedQueue(Queue):
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if not self.is_empty():
            removed = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return removed
        else:
            print("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            print("Queue is empty")

    def is_empty(self):
        return self.head is None

    def is_full(self):
        # LinkedQueue doesn't have a max size
        return False
