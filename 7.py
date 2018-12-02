class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #if x is bigger/smaller than max/min value or if x is equal to 0
        maxandmin = (2 ** 31) - 1
        if x > maxandmin or x < -maxandmin-1 or x == 0:
            return 0
        
        #if x is smaller than 0, which means it's a negative number
        if x < 0:
            #remove the minus sign
            x = -x
            strx = str(x)
            #reverse the number
            intx = int(strx[::-1])
            #if output is bigger than max value
            if intx > maxandmin+1:
                return 0
            else:
                #re-add the minus sign, turning into a negative number
                intx = -intx
                return intx
            
        #if x is bigger than 0, which means it's positive
        if x > 0:
            strx = str(x)
            #reverse the number
            intx = int(strx[::-1])
            #if output is bigger than max value
            if intx > maxandmin:
                return 0
            else:
                return intx
    
