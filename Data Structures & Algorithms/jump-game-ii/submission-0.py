class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums) 
        dp =[10**9] * n
        dp[-1] = 0

        i = n -2 
        while i > -1:
            end = min(n, i + nums[i] + 1)
            for j in range(i + 1, end) : 
                dp[i] = min(dp[i], 1+dp[j])
            i -= 1

        return dp[0]


