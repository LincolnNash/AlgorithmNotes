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
        self.array = self.original
        return self.array


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        self.array = self.original
        for i in range(len(self.array)):
            j = random.randint(0,len(self.original)-1)
            temp = self.array[i]
            self.array[i] = self.array[j]
            self.array[j] = temp
        return self.array

a = [1,2,3,4,5,6]
c = a[::-1]
print(id(a), id(c))