class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        result = []
        for s in strs : 
            alphabet = [0]*26
            for c in s: 
                index = ord('z') - ord(c)
                alphabet[index] += 1
            alpha_str = ','.join(map(str,alphabet))

            if alpha_str in hashmap :
                hashmap[alpha_str].append(s)
            else : 
                hashmap[alpha_str] = [s]
        
        for key, val in hashmap.items():
            result.append(val) 
        return result


