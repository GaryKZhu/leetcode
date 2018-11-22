class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        longest = 0
        for i in range(length):
            seen = set()
            for x in range(i, length):
                if s[x] in seen: break
                seen.add(s[x])
            longest = max(len(seen), longest)
        return longest
 
