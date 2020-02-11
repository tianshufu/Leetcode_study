class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #define a num to record the number of 0
        num=0
        for i in nums:
            if(i==0):
                nums.remove(i)
                num+=1
                nums.append(0)
        return nums

if __name__ == '__main__':
    print(Solution.moveZeroes(Solution,[1,3,0,0,4]))


