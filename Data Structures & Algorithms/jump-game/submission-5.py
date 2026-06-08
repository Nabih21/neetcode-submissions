class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) 


        dist = 1
        r = n -2
        while r > -1:
            if nums[r] >= dist :
                dist = 1
            else:
                dist += 1
            r -= 1
        if dist > 1:
            return False
        return True
