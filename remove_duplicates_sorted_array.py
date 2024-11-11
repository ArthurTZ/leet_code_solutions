# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element 
# appears only once. The relative order of the elements should be kept the same. 
# Then return the number of unique elements in nums

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p1 = 0 # pointer

        for p2 in range(1,len(nums)):
            if nums[p2] != nums[p1]:
                p1+=1
                nums[p1] = nums[p2]
        num = p1 + 1
        return num        


