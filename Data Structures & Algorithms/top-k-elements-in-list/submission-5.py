class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = []
 
        for i in range(len(nums)+1):
            bucket.append([])

        print(bucket)
        seen = {}
        res = []

        for n in nums:
            seen[n] = seen.get(n, 0) + 1
        

        for key, value in seen.items():
            print(key, value)
            bucket[value].append(key)
            print(bucket)

        
 
        bucket.reverse()
        print(bucket)

        for b in bucket :
            for n in b:
                res.append(n)
                if len(res) == k:
                    return res
                    
        return res
