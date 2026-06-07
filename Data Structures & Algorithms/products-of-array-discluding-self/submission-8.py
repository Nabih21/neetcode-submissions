class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix = []

        # prefix.append(nums[0])
        n = len(nums)    
        prefix =  [1] * n
        suffix =  [1] * n

        suffix[n -1] = nums[n -1]
        prefix[0] = nums[0]

        for i in range(1, n):

            prefix[i] = nums[i] *prefix[i-1]
            # prefix[i] = nums[i-1] *prefix[i-1]
        
        for i in range(n-2, -1, -1):
            suffix[i] = nums[i] * suffix[i+1]
            # suffix[i] = nums[i+1] * suffix[i+1]
        
        print(prefix)
        print(suffix)

        res = []
        res.append(suffix[1]) 
        for i in range(1,n):
            if i < n-1:
                res.append(prefix[i-1] * suffix[i+1] )
            else :
                res.append(prefix[i-1])
        return res 

        