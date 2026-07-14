# solved using tuple and dict,
# this similar to the ideal state of time and space complexity given
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        main_dict = {}

        for i in range(len(strs)):
            first_list = [0]*26

            for char in strs[i]:
                first_list[(ord(char) - ord('a'))] += 1
            
            key_list = tuple(first_list)
            if key_list not in main_dict:
                main_dict[key_list] = []
                main_dict[key_list].append(strs[i])
            else:
                main_dict[key_list].append(strs[i])

        answer = list(main_dict.values())
        return answer
