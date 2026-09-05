# without py's built in method .isalnum()
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) -1
        while(i<j):
            if 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z' or '0' <= s[i] <= '9':
                if 'a' <= s[j] <= 'z' or 'A' <= s[j] <= 'Z' or '0' <= s[j] <= '9':
                    if s[i].lower() == s[j].lower():
                        i += 1
                        j -=1
                    else: 
                        return False
                else: 
                    j -= 1
            else:
                i += 1
        return True