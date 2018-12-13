class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # initialize 
        stack = []
        
        reference = {")": "(", "}": "{", "]": "["}

        # loop through s
        for char in s:

            if char in reference:

                top_element = stack.pop() if stack else 'err'

                
                if reference[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
