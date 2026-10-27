#nums =[1,2,3,1]
class Solution:
    def containsDuplicate(self,nums:list[int])->bool:
        duplicateSet=set()
        for n in nums:
            if n in duplicateSet:
                return True
            duplicateSet.add(n)
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.containsDuplicate([1,1,1,2, 3, 1]))  # True
    print(s.containsDuplicate([1, 2, 3, 4]))  # False
    print(s.containsDuplicate([]))            # False