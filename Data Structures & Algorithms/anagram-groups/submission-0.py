# solved using dict
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        dict_s = {}
        for i in range(len(strs)):
            if "".join(sorted(strs[i])) not in my_dict:
                my_dict["".join(sorted(strs[i]))] = []
            my_dict["".join(sorted(strs[i]))].append(strs[i])
        answer = list(my_dict.values())
        return answer