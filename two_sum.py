### - BIG O(n^2)
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



### - BIG O(n)
def twoSum(self, nums : list[int], target : int):
    hash_table = dict()

    for idx,value in enumerate(nums):
        comp = target - value

        if comp in hash_table:
            return hash_table[comp], idx
        
        hash_table[value] = idx 