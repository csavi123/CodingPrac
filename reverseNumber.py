class Solution:
    def reverse(self, x: int) -> int:
        reversed_num=0
        original=x
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x>0:
            reversed_num=reversed_num*10+x%10
            x//=10
        reversed_num=reversed_num * sign
       
        if reversed_num < -2147483648 or reversed_num > 2147483647:
            return 0
        return reversed_num
if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123))  # 321
    print(s.reverse(-123))  # -321
    print(s.reverse(120))  # 21

#The time complexity is O(log₁₀ n) because the number of iterations depends on the number of digits in the input integer, which scales logarithmically with the value of the number,
#and the space complexity is O(1) because you only allocate a single integer variable (reversed_num) to track the reversed number.