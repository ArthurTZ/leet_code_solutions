# Have to find if the parameter number is read as the same from right to left and vice versa
# have to compare the first char of the string with the last char of the string
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        lista = [x for x in x]


        for idx, val in enumerate(lista):
            if idx >= len(lista) // 2:
                break
            if val != lista[-(idx +1)]:
                return False
                break 
        return True

x = '121'
print(Solution().isPalindrome(x))
                            

        

        