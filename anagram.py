class Solution:
    def isAnagram(self,str1:str,str2:str)->bool:
        
        str1,str2=str1.lower(),str2.lower()
        str1=str1.replace(" ","")
        str2=str2.replace(" ","")
        if len(str1)!=len(str2):
            return False
        count=[0]*26
        for ch in str1:
            count[ord(ch)-ord('a')]+=1
        
        for ch in str2:
            count[ord(ch)-ord('a')]-=1

        for c in count:
            if c!=0:
                return False
        return True

solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))   # True
print(solution.isAnagram("rat", "car"))           # False
print(solution.isAnagram("Dormitory", "Dirty room"))  # True

#Space complexity is O(1) because the count array has a fixed size of 26, regardless of the input size. 
#The time complexity is O(n), where n is the length of the input strings, as we iterate through both strings once to populate and check the count array.