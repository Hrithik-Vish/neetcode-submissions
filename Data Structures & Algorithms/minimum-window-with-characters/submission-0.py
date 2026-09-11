class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        i = 0
        j = 0
        i_best = 0
        j_best = 0
        min_s = float('inf')
        t_dict = {}
        need = 0
        s_dict = {}
        have = 0

        for char in t:
            t_dict[char] = t_dict.get(char, 0) +1
        need = len(t_dict)

        while(j != len(s)):
            s_dict[s[j]] = s_dict.get(s[j], 0) +1

            if s[j] in t_dict:
                if s_dict[s[j]] == t_dict[s[j]]:
                    have += 1 

            while need == have:

                if min_s > (j - i + 1):
                    min_s = (j - i + 1)
                    i_best = i 
                    j_best = j

                if s[i] in t_dict:
                    if s_dict[s[i]] == t_dict[s[i]]:
                        have -= 1 

                if (s_dict[s[i]] != 1):
                    s_dict[s[i]] -= 1
                else: 
                    del s_dict[s[i]]
                
                i += 1

            j+=1

        if min_s == float('inf'):
            return ""
        output = s[i_best:j_best+1]
        return output
        

        

            