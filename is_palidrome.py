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
        return True


# print(Solution().isPalindrome(x))

# otimização para O(N)
class Solution(object):
    def isPalindrome(self, x):

        x = str(x)

        if x < 0:
            return False
        
        for idx in range(len(x) // 2):
            if x[idx] != x[-(idx + 1)]:
                return False
            
        return True

        

#        