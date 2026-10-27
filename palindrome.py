class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num=0
        original=x
        if x<0:
            return False
        while x>0:
            reversed_num=reversed_num*10+x%10
            x//=10
        return reversed_num==original
if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(121))  # True
    print(s.isPalindrome(-121))  # False
    print(s.isPalindrome(10))  # False

#The time complexity is O(log₁₀ n) because the number of iterations depends on the number of digits in the input integer, which scales logarithmically with the value of the number,
#and the space complexity is O(1) because you only allocate a single integer variable (reversed_num) to track the reversed number.