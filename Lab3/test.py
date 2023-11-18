from array_stack import ArrayStack
from linked_stack import LinkedStack
from fixed_array_stack import FixedArrayStack
from array_queue import ArrayQueue
from linked_queue import LinkedQueue

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

    print("\nTesting FixedArrayStack:")
    fixed_array_stack = FixedArrayStack(3)
    fixed_array_stack.push('x')
    fixed_array_stack.push('y')
    fixed_array_stack.push('z')
    print(fixed_array_stack.pop())  # Expected output: 'z'
    print(fixed_array_stack.peek())  # Expected output: 'y'

def test_queues():
    print("Testing ArrayQueue:")
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

if __name__ == "__main__":
    test_stacks()
    test_queues()
