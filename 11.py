class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #First Solution, Time limit exceeded ;c
        largest = 0
        
        for i in range (0, len(height)):
            for j in range (i, len(height)):
                ht = min(height[i],height[j])
                base = j - i
                area = ht * base
                largest = max(area, largest)
                
        return largest
        
        #Second Solution, with 2 pointers
        
        #Initalize variables
        area = 0
        p1 = 0
        p2 = len(height)-1
        
        #While loop
        while p2 > p1:
            #If p1 is greater
            if height[p1] > height[p2]:
                #Area is the distance between p2 and p1 times the lower value
                area = max(area, (p2 - p1) * height[p2])
                #Move the lower value in one position
                p2 = p2 - 1
                
            #If p2 is greater or if they are equal
            else:
                area = max(area, (p2 - p1) * height[p1])
                p1 = p1 + 1
        return area
