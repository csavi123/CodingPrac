class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left=0
        right=len(heights) - 1
        maxArea=0
        while(left<right):
            area = min(heights[left], heights[right]) * (right-left)
            maxArea=max(area,maxArea)

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxArea
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))  # 49