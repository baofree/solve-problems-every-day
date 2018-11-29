class MyHashSet:
    size = 1000001

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [False] * self.size

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.data[key] = True

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.data[key] = False

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return self.data[key]


if __name__ == '__main__':
    hashSet = MyHashSet()
    hashSet.add(1)
    hashSet.add(2)
    hashSet.contains(1)
    hashSet.contains(3)
    hashSet.add(2)
    hashSet.contains(2)
    hashSet.remove(2)
    hashSet.contains(2)
    hashSet.add(5)
