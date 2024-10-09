
### - BIG O(n2)
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        prefix = ""

        min_len = min(len(word) for word in strs)
        for idx in range(min_len):
            current = strs[0][idx]
            for word in strs:
                if word[idx] != current:
                    return prefix
            prefix += current    
        return prefix
    


### - otimização BIG O(n log n)


class Solution(object):
    def longestCommonPrefix(self,strs: list[str]):

        if not strs: return ""

        result = []
        strs.sort()
        first = strs[0]
        last = strs[-1]

        for idx in range(min(len(first)), len(last)):
            if first[idx] != last[idx]:
                break
            result.append(first[idx])
        string = ''.join(result)
        return string

    


