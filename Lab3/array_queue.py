from abstract_queue import Queue


class ArrayQueue(Queue):
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = []

    def enqueue(self, item):
        if not self.is_full():
            self.queue.append(item)
        else:
            print("Queue is full")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty")

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.max_size
