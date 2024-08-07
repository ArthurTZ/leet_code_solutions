class Solution(object):
    def twoSum(self, nums : list[int], target : int):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ### uma lista de inteiros, e um alvo, esse alvo ele é a soma de alguns dos valores que estao dentro da lista, so que deve retornar o indice em vez dos numeros
        for i in range(len(nums)):
            for j in range(i +1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

        
nums = [3,2]
target = 5
        

objet = Solution().twoSum(nums=[3,2], target=5)        
print(objet)