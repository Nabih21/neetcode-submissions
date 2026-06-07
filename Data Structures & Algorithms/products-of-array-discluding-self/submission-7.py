class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [0]* len(nums)
        prod = 0
        zeroCount = 0 

        for n in nums :
            if n == 0:
                zeroCount += 1
                continue

            if prod == 0 :
                prod = n
            else:
                prod *= n

        if zeroCount > 1:
            prod = 0
            
        for i in range(len(nums)):
            if nums[i] != 0  :
                if zeroCount > 0:
                    products[i] = 0
                else: 
                    products[i] = int(prod/nums[i])
            else : 

                products[i] = prod
        
        return products
        