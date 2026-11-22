class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0
        l,r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        result=0
        while l<r:
            if leftMax <= rightMax:
                l = l+1
                leftMax = max(leftMax, height[l])
                result+= leftMax - height[l]
            else:
                r =r-1
                rightMax = max(rightMax, height[r])
                result+= rightMax - height[r]
        return result
if __name__ == "__main__":
    s = Solution()
    print(s.trap([0,2,0,3,1,0,1,3,2,1]))