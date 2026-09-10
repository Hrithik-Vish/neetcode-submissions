class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = 0
        s1_counter = {}
        window_counter = {}

        for char in s1:
            s1_counter[char] = s1_counter.get(char, 0) +1
        
        while(j != len(s2)):
            window_counter[s2[j]] = window_counter.get(s2[j], 0) +1


            while(j-i+1) > len(s1):
                if window_counter[s2[i]] != 1:
                    window_counter[s2[i]] -= 1
                else:
                    del window_counter[s2[i]]
                i += 1

            if s1_counter == window_counter:
                return True
            j += 1

        return False