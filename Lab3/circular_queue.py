from abstract_queue import Queue


class CircularQueue(Queue):
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = 0  # Index of the front element
        self.rear = -1  # Index of the rear element
        self.size = 0    # Current size of the queue

    def enqueue(self, item):
        if not self.is_full():
            # Calculate the next rear index in a circular manner
            self.rear = (self.rear + 1) % self.max_size
            self.queue[self.rear] = item
            self.size += 1
        else:
            print("Queue is full")

    def dequeue(self):
        if not self.is_empty():
            removed = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return removed
        else:
            print("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[self.front]
        else:
            print("Queue is empty")

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size
