class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ""
        if len(s) < 2:
            return s
        for i in range(0, len(s)):
            for j in range(0, i+1):
                ss = s[j:len(s)-i+j]
                if ss == ss[::-1]:
                    return ss
