from array_stack import ArrayStack
from linked_stack import LinkedStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue
from circular_queue import CircularQueue  
from dict_stack import DictStack  

def test_stacks():
    print("Testing ArrayStack:")
    array_stack = ArrayStack(5)
    array_stack.push(1)
    array_stack.push(2)
    print(array_stack.pop())  # Expected output: 2
    print(array_stack.peek())  # Expected output: 1

    print("\nTesting LinkedStack:")
    linked_stack = LinkedStack()
    linked_stack.push('a')
    linked_stack.push('b')
    print(linked_stack.pop())  # Expected output: 'b'
    print(linked_stack.peek())  # Expected output: 'a'

    print("\nTesting DictStack:")
    dict_stack = DictStack()
    dict_stack.push('key1', 'value1')
    dict_stack.push('key2', 'value2')
    print(dict_stack.pop())  # Expected output: ('key2', 'value2')
    print(dict_stack.peek())  # Expected output: ('key1', 'value1')

def test_queues():
    print("\nTesting ArrayQueue:")
    array_queue = ArrayQueue(4)
    array_queue.enqueue('apple')
    array_queue.enqueue('banana')
    print(array_queue.dequeue())  # Expected output: 'apple'
    print(array_queue.peek())  # Expected output: 'banana'

    print("\nTesting LinkedQueue:")
    linked_queue = LinkedQueue()
    linked_queue.enqueue(10)
    linked_queue.enqueue(20)
    print(linked_queue.dequeue())  # Expected output: 10
    print(linked_queue.peek())  # Expected output: 20

    print("\nTesting CircularQueue:")
    circular_queue = CircularQueue(3)
    circular_queue.enqueue('red')
    circular_queue.enqueue('green')
    circular_queue.enqueue('blue')
    print(circular_queue.dequeue())  # Expected output: 'red'
    print(circular_queue.peek())  # Expected output: 'green'
    circular_queue.enqueue('yellow')
    print(circular_queue.dequeue())  # Expected output: 'green'
    print(circular_queue.peek())  # Expected output: 'blue'

if __name__ == "__main__":
    test_stacks()
    test_queues()
