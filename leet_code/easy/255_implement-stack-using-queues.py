class MyQueue:

    def __init__(self):
        self.data = []

    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.empty():
            return None
        return self.data.pop(0)

    def top(self):
        if self.empty():
            return None
        return self.data[0]

    def empty(self):
        if self.data:
            return False
        return True


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = MyQueue()

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.data.push(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        result = None
        if self.empty():
            return result

        temp_data = MyQueue()
        while not self.data.empty():
            result = self.data.pop()
            if not self.data.empty():
                temp_data.push(result)
        self.data = temp_data
        return result

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            return None
        temp_data = MyQueue()
        while not self.data.empty():
            result = self.data.pop()
            temp_data.push(result)
        self.data = temp_data
        return result

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.data.empty()


if __name__ == '__main__':
    # queue = MyQueue()
    # print(queue.empty())
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    print(obj.pop())
    print(obj.top())
    print(obj.empty())
