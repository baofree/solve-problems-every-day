"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.data.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.data:
            return self.data.pop()
        return None

    def top(self):
        """
        :rtype: int
        """
        if self.data:
            return self.data[-1]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if self.data:
            return min(self.data)
        return None


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    print(minStack.pop())
    print(minStack.top())
    print(minStack.getMin())
