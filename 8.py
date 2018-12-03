class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        sign = 1
        digits = "0123456789"
        num = ''
        
        #remove whitespace
        str = str.strip()   
        
        #check string is empty
        if len(str) == 0:
            return 0
        
        #check first character
        if str[0].isdigit() == False:
            if str[0] == '-':
                str=str[1:]
                sign = -1
            elif str[0] == '+':
                str=str[1:]
            else:
                return 0
            
        ##check string not empty
        if len(str) == 0:
            return 0
    
        if str[0].isdigit() == False:
            return 0
        
        # iterate through string 
        for x in str:
            #if x is a number
            if x.isdigit():
                num += x 
                print(num)
            #after find a non digit character
            else:
                break
                
        #maxinum and mininum value comparison
        maxandmin = (2 ** 31) - 1
        if int(num)*sign > maxandmin:
            return maxandmin
        if int(num)*sign < -(maxandmin) - 1:
            return -(maxandmin) -1
        return int(num)*sign
