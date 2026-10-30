class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hashmap={}
        count=[[] for _ in range(len(nums)+1)]
        for n in nums:
            if n in hashmap:
                hashmap[n]+=1
            else:
                hashmap[n]=1
        result=[]
        for key,freq in hashmap.items():
            count[freq].append(key)
        for i in range(len(count)-1,0,-1):
            for n in count[i]:
                result.append(n)
                if len(result)==k:
                    return result
solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))  # [1,2]
#Space complexity is O(1) because the count array has a fixed size of 26, regardless of the input size. 
#The time complexity is O(n), where n is the length of the input strings, as we iterate through both strings once to populate and check the count array.