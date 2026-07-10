from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return Counter(s) == Counter(t)

'''
        below is the handmade counter to understand the 
        logic behind this without using any library import
'''
        # dict_s = {}
        # dict_t = {}

        # for char in s:
        #     dict_s[char] = dict_s.get(char, 0) +1
        # for char in t:
        #     dict_t[char] = dict_t.get(char,0) +1
        
        # return dict_s == dict_t