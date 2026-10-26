class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        sum=0
        for i in nums:
            sum=sum+i    
        return(sum%k)
if __name__ == "__main__":
    s = Solution()
    print(s.minOperations([2, 3, 4, 5], 2))  # 0

#Time complexity is O(n) because the for loop iterates through the list exactly once, 
#and the space complexity is O(1) because you only allocate a single integer variable (sum) to track the running total.