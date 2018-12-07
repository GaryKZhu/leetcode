class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        LCP = ''
        if len(strs) == 0:
            return ""
        shortest = min(strs,key = len)
        for i in range(0, len(shortest)):
            charstr = shortest[i]
            for x in strs:
                if charstr != x[i]:
                    return LCP
            LCP += charstr
        return LCP
