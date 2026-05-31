class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        prefix = []
        suffix = []

        max = 0
        for i in range(len(height)):
            if height[i] > max :
                max = height[i] 
            prefix.append(max)

        max = 0 
        for i in range(len(height) -1, -1, -1):
            if height[i] > max :
                max = height[i]
            suffix.append(max)
        
        suffix.reverse()
        
        for i in range(len(height)):
            res += min(prefix[i], suffix[i]) - height[i] 


        return res
        