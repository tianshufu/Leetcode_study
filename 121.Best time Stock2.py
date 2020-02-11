class Solution:
    def maxProfit(self, prices) -> int:
        if not prices:
            return 0;

        else:
         profit=0
         for i in range(1,len(prices)):
                #define a value to store the money earned by each dat
                tmp=prices[i]-prices[i-1]
                if (tmp>0):
                    profit+=tmp
        return profit







if __name__ == '__main__':
   print( Solution.maxProfit(Solution,[1,2,3,4,7]))