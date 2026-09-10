class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        most_freq_char = 0
        max_len = 0
        freq_dict = {}

        while(j != len(s)):

            freq_dict[s[j]] = freq_dict.get(s[j], 0) + 1

            most_freq_char = max(freq_dict.values())

            while((j-i+1) - most_freq_char > k):
                freq_dict[s[i]] -= 1
                i += 1

            if max_len < (j-i+1):
                max_len = (j-i+1)

            j += 1

        return max_len

        












                   