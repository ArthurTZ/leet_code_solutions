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




