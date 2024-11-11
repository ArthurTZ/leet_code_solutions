
# 3ms - O(n)

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        for char in range(len(haystack) - len(needle) + 1):
            if haystack[char:char + len(needle)] == needle:
                return char
        return -1    


