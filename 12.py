class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        

        Roman = ''
        while num > 0:
            if num >= 1000:
                num -= 1000
                Roman += 'M'
                continue
            if num >= 900:
                num -= 900
                Roman += 'CM'
                continue
            if num >= 500:
                num -= 500
                Roman += 'D'
                continue
            if num >= 400:
                num -= 400
                Roman += 'CD'
                continue
            if num >= 100:
                num -= 100
                Roman += 'C'
                continue
            if num >= 90:
                num -= 90
                Roman += 'XC'
                continue
            if num >= 50:
                num -= 50
                Roman += 'L'
                continue
            if num >= 40:
                num -= 40
                Roman += 'XL'
                continue
            if num >= 10:
                num -= 10
                Roman += 'X'
                continue
            if num >= 9:
                num -= 9
                Roman += 'IX'
                continue
            if num >= 5:
                num -= 5
                Roman += 'V'
                continue
            if num >= 4:
                num -= 4
                Roman += 'IV'
                continue
            if num >= 1:
                num -= 1
                Roman += 'I' 
        return Roman
