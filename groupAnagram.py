class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap={}
        for i in strs:
            count=[0]*26
            for j in i:
                c=ord(j)-ord('a')
                count[c]+=1
            key=tuple(count)
            if key not in hashmap:
                hashmap[key]=[]
            hashmap[key].append(i)
        return list(hashmap.values())
solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))  # [["eat","tea","ate"],["tan","nat"],["bat"]]

#Space complexity is O(1) because the count array has a fixed size of 26, regardless of the input size. 
#The time complexity is O(n), where n is the length of the input strings, as we iterate through both strings once to populate and check the count array.