class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in seen:
                return[seen[diff],i] 
            seen[n]=i 
        return []
if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9)) 