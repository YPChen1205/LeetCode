import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.array = nums
        self.original = nums
    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original

    def shuffle(self):
        """
        shuffle the array with equal probability
        :rtype: List[int]
        """
        array_len = len(self.array)
        for i in range(array_len):
            # select an element
            selected_idx = random.randrange(i, array_len)
            # swap with the index i
            temp = self.array[i]
            self.array[i] = self.array[selected_idx]
            self.array[selected_idx] = temp
        return self.array