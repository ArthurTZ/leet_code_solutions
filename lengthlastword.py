# class Solution(object):
#     def lengthOfLastWord(self, s : str):
#         """
#         :type s: str
#         :rtype: int
#         """

#         new = s.strip()



s = "Hello World"
s1 = "   fly me   to   the moon  "

word = s1.split()

last = word[-1]
print(len(last))
