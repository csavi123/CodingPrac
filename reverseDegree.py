class Solution:
    def reverseDegree(self, s: str) -> int:
        hashMap={}
        for i,ch in enumerate(s.lower(),start=1):
            
            if ch.isalpha():
                revValue=123-ord(ch)
                hashMap[i]=revValue

        finalValue=sum(key*value for key,value in hashMap.items())
        return finalValue
if __name__ == "__main__":
    s = Solution()
    print(s.reverseDegree("abc"))  # 1*25 + 2*24 + 3*23 = 25 + 48 + 69 = 142

#Both the time complexity and space complexity are O(n), where n is the length of the string