class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for c in s:
            dict1[c] = dict1.get(c, 0) + 1
        
        for c in t:
            dict2[c] = dict2.get(c, 0) + 1
        
        if len(dict1) != len(dict2) :
            return False

        for c in dict1 :
            if dict1.get(c) != dict2.get(c) :
                return False
        
        return True


        
