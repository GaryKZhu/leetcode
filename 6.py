class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        row = [''] * numRows
        index = 0
        
        i = 1
        for x in s:
            row[index] += (x)
            if index == 0:
                i = 1
            elif index == numRows -1:
                i = -1
            index = index + i 
             
            
        return ''.join(row)
