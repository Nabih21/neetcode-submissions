class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max = [[] for _ in range(len(nums) + 1)]
        hashmap = {}
        result = []
        reverseIndex = len(nums) 

        for x in nums : 
            hashmap[x] = hashmap.get(x, 0) + 1

        for key, val, in hashmap.items():
            max[val].append(key) 
        
        while len(result) < k: 
            if max[reverseIndex]:
                for i in max[reverseIndex] :
                    if len(result) == k:
                        break
                    result.append(i)
            reverseIndex -= 1
        
        return result
