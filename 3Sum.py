class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result=set()
        for i in range(len(nums)-1):
            seen=set()
            target=-nums[i]
            for x in nums[i+1:]:
                if target-x in seen:
                    triplet = [nums[i], target-x, x]
                    triplet = sorted(triplet)
                    triplet = tuple(triplet)
                    result.add(triplet)
                seen.add(x)
        answer = []
        for t in result:            # t = each tuple, e.g. (-1, 0, 1)
            answer.append(list(t))  # turn it into [-1, 0, 1] and add it
        return answer
        
solution = Solution()
print(solution.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1, 0, 1], [-1, -1, 2]]

#Time and space complexity is O(n)