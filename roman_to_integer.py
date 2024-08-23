
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
                                """
romans = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
total = 0  # vai pegar o numero do total do numero selecionado no caso é " S "
s = "MCMXCIV"
for idx, val in enumerate(s):
    if idx < len(s) - 1 and romans[val] < romans[s[idx + 1]]:
        total -= romans[val]
    else:
        total += romans[val]    

print(total)
