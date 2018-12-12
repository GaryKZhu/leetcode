#Brute Force(Time Limit Exceeded)
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
solution = []
        answer = []
        for x in range(0, len(nums)):
            for y in range(x+1, len(nums)):
                for z in range(y+1, len(nums)):
                    if nums[x] + nums[y] + nums[z] == 0:
                        answer.append(nums[x])
                        answer.append(nums[y])
                        answer.append(nums[z])
                        if sorted(answer) in solution:
                            answer = []
                            continue
                        else:
                            solution.append(sorted(answer))
                            answer = []
                            continue
        return solution
        
#Two Pointer Solution
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        #sort list
        nums.sort()
        #run through exceptions
        if len(nums) < 3:
            return []
        if all(v == 0 for v in nums):
            return [[0,0,0]]
        #initalize result list
        result = []
        
        #loop through nums
        
        for i in range(len(nums)):
            #if i is the same as previous value
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
                
            #set target, which is negative i
            
            target = nums[i] * -1
            
            #set pointers
            
            leftpoint = i+1
            rightpoint = len(nums)-1
            
            #if leftpoint is smaller than rightpoint
            
            while leftpoint<rightpoint:
                #if they add up to negative i append
                if nums[leftpoint]+nums[rightpoint] == target:
                    result.append([nums[i], nums[leftpoint], nums[rightpoint]])
                    
                    #increase leftpoint value, as there still might be more values
                    leftpoint += 1
                    
                    #if leftpoint is equal to one before it(or if multiple are)
                    while leftpoint < rightpoint and nums[leftpoint] == nums[leftpoint-1]:
                        leftpoint += 1
                    
                        
                #if the added value is smaller, than increase leftpoint value
                elif nums[leftpoint] + nums[rightpoint] < target:
                    leftpoint = leftpoint+1
                    
                #if the added value is larger, than decrease rightpoint value
                else:
                    rightpoint = rightpoint-1
                    
        return result
