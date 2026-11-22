class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closing_bracket={")":"(","}":"{","]":"["}
        for char in s:
            if char in closing_bracket:  #checks the keys
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = "#"
                if closing_bracket[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
if __name__ == "__main__":
    s = Solution()
    print(s.isValid("["))

    #with Time Complexity O(n) and time complexity is O(n)