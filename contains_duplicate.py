class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        new = set()

        for n in nums:
            if n in new:
                return True
            else:
                new.add(n)
        return False

        