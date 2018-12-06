class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Initializing variables
        result = 0
        
        for x in range(0,len(s)):
            
            if s[x] == "M":
                result += 1000
                
            if s[x] == "D":
                result += 500
                
            if s[x] == "C":
                if x + 1 != len(s) and s[x+1] == "M":
                    result -= 100
                    continue
                    
                if x + 1 != len(s) and s[x+1] == "D":
                    result -= 100
                    continue
                    
                result += 100
                
            if s[x] == "L":
                result += 50
                
            if s[x] == "X":
                if x + 1 != len(s) and s[x+1] == "C":
                    result -= 10
                    continue
                    
                if x + 1 != len(s) and s[x+1] == "L":
                    result -= 10
                    continue
                    
                result += 10
                
            if s[x] == "V":
                result += 5
                
            if s[x] == "I":
                if x + 1 != len(s) and s[x+1] == "X":
                    result -= 1
                    continue
                    
                if x + 1 != len(s) and s[x+1] == "V":
                    result -= 1
                    continue
                    
                result += 1
                
        return result
