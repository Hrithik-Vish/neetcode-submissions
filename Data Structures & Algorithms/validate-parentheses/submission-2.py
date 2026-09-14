class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []
        hash_map = {")": "(", "]": "[", "}": "{"}

        for char in s:

            if char in hash_map:
                if not open_stack:
                    return False
                if hash_map[char] != open_stack.pop():
                    return False 
            else:

                open_stack.append(char)
        
        if not open_stack:
            return True
            
        return False
            
