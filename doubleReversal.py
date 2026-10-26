#nums =[1,2,3,1]
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or num % 10 != 0
            

if __name__ == "__main__":
    s = Solution()
    print(s.isSameAfterReversals(526))  # True
    print(s.isSameAfterReversals(1800))  # False
    print(s.isSameAfterReversals(0))  # True    