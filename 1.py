#Solution 1
class Solution:
    def twoSum(self, nums, target):
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if((nums[i] + nums[j]) == target):
                    return i,j
                
#Solution 2
class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for index, num in enumerate(nums):
            if target - num in dict:
                return [dict[target - num], index]
            dict[num] = index 
