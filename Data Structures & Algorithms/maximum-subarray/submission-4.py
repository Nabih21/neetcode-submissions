class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: 
            return 0

        sum = nums[0] 
        current = sum

        for i in range(1, len(nums)):
            if current > 0 : 
                current += nums[i] 
            
            else : 
                current = nums[i] 

            sum = max(sum, current) 


        return sum

