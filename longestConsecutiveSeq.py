class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s=set()
        best=0
        for n in nums:
            s.add(n)
            
        for n in s:
            if n-1 not in s:
                current=n
                l=1
                while current+1 in s:
                    current=current+1
                    l=l+1
                if l>best:
                    best=l
        return best
solution = Solution()
print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4

#Time and space complexity is O(n)