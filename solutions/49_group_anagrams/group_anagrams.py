from ast import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in dict:
                dict[key].append(s)
            else:
                dict[key] = [s]
        return list(dict.values())