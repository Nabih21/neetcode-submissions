class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = [] 

        for s in strs: 

            temp = [0] * 26
            for c in s : 
                index = ord(c) - ord('a') 
                temp[index] += 1

            temp = ','.join(map(str, temp))
            hashmap[temp] = hashmap.get(temp, [])
            hashmap[temp].append(s)
        
        for s in hashmap :
            res.append(hashmap.get(s))
        return res


