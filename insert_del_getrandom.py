import random
class RandomizedSet(object):
    '''  All the  operation should be complete in O(1)
        The idea of this sollution is using hashtable and list, where we can randomly chose an element.
        using hash_table map make checking exists, adding, and removing element being done in O(1)
        in python we can use the build_in structure Set

    '''
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.set:
            self.set.add(val)
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            self.set.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        idx = random.randrange(len(self.set))
        lst = list(self.set)
        return lst[idx]

