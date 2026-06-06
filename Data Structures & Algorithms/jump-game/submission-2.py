class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 2
        dist = 1

        while i >= 0 :
            if nums[i] >= dist :
                if i == 0 :
                    return True
                i -= 1
                dist = 1
            elif nums[i] < dist : 
                if i == 0:
                    return False
                i -= 1 
                dist += 1
 

                
            
        
        return True 