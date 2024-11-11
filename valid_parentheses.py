# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        symbols = {"(", "{", "["}
        matching = {")": "(", "]": "[", "}": "{"} 

        stack = 0

        for char in s:
            if char in symbols:
                stack.append(char)
            else:
                if stack and stack[-1] == matching[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0                

            
