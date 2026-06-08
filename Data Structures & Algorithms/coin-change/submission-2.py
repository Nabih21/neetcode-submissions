class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: 
            return 0
        dp = [amount+1] * (amount + 1) 

        dp[0] =0 
        minSum = amount + 1
        # dp[coins[0]] = 1

        for i in range( 1, amount+1 ):
            for c in coins: 
                if c <= i: 
                    dp[i] = min(dp[i], 1 + dp[i-c])
        
        # for c in coins:
        #     minSum = dp[amount -c]
        
        
        print(dp)
        if dp[amount] > amount  :
            return -1
        return dp[amount]



        