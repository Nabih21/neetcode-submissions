class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) -1

        maxL = height[l]
        maxR = height[r] 
        sum = 0

        while l < r:
            if maxL <= maxR :
                temp = min(maxL, maxR) - height[l]
                if temp > 0:
                    sum += temp
                l += 1 
                maxL = max(maxL, height[l])
            else : 
                temp = min(maxL, maxR) - height[r]
                if temp > 0:
                    sum += temp
                r -= 1 
                maxR = max(maxR, height[r])


        return sum
        