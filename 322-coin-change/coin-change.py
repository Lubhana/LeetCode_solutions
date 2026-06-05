class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1]*(amount+1)# creates a list of lenght amount+1 and value of each index is also amount+1
        dp[0]=0
        for i in range(1,amount+1):
            for c in coins:
                if (i-c)>=0:
                    dp[i]=min(dp[i],1+dp[i-c])# 1+dp[i-c]= 1+no of coins required to reach previous index of dp
        return dp[amount] if dp[amount]!= amount+1 else -1


