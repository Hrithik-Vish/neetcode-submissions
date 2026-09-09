class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        i = 0
        j = 0

        max_len = 0
        if len(s) > 0:
            max_len = 1

        while(j != (len(s))):

            if s[j] not in substring:
                substring.add(s[j])
                j += 1
            else:
                while(s[j] in substring):
                    substring.remove(s[i])
                    i += 1
                substring.add(s[j])
                j += 1
            if max_len <=  len(substring):
                max_len = len(substring)

        return max_len
                



