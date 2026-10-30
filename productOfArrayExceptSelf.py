from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        leftList=[1]*n
        rightList=[1]*n
        finalOutput=[1]*n
        left,right=1,1
        for i in range(n):
            leftList[i]=left
            left=left*nums[i]
        for j in range(n-1,-1,-1):
            rightList[j]=right
            right=right*nums[j]
        for count in range(n):
            finalOutput[count]=leftList[count]*rightList[count]
        return finalOutput
if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))  # [24,12,8,6]

#Both the time complexity and space complexity are O(n), where n is the length of the input list.