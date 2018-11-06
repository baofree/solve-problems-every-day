"""
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size,
and is empty operations are valid.
Depending on your language, stack may not be supported natively.
You may simulate a stack by using a list or deque (double-ended queue),
as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

"""


class MyStack:
    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)
        pass

    def pop(self):
        if self.empty(): return None
        return self.data.pop(-1)

    def peek(self):
        if self.empty(): return None
        return self.data[-1]

    def empty(self):
        return not self.data


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = MyStack()

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        if self.empty():
            self.data.push(x)
        else:
            temp = MyStack()
            while not self.data.empty():
                temp.push(self.data.pop())
            self.data.push(x)
            while not temp.empty():
                self.data.push(temp.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty(): return None
        return self.data.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.empty(): return None
        return self.data.peek()

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.data.empty()


if __name__ == '__main__':
    # stack = MyStack()
    # print(stack.empty())
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # print(stack.empty())
    # print(stack.peek())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    obj = MyQueue()
    print(obj.empty())
    obj.push(1)
    obj.push(2)
    obj.push(3)
    print(obj.peek())
    print(obj.pop())
    print(obj.empty())
    print(obj.pop())
    print(obj.pop())
