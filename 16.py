class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        answer = nums[0]+nums[1]+nums[2]
        nums.sort()
        #loop through nums
        
        for i in range(len(nums)):
            #if i is the same as previous value
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            #set pointers
            
            leftpoint = i+1
            rightpoint = len(nums)-1
            
            #if leftpoint is smaller than rightpoint
            
            while leftpoint<rightpoint:
                #initialize temporary sum 
                tempsum = nums[leftpoint]+nums[rightpoint]+nums[i]
                
                #if the difference is smaller tempsum is the new answer
                if abs(target-tempsum) < abs(target-answer):
                    answer = tempsum
                    
                #if the tempsum is smaller than the target move the first pointer in one, making tempsum larger
                if tempsum < target:
                    leftpoint += 1
                
                #else, move the second pointer in one, making tempsum smaller
                else:
                    rightpoint -= 1        
        return answer
