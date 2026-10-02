class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        string_dict = dict()
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in string_dict:
                string_dict[sorted_s] = []
                string_dict[sorted_s].append(s)
            else:
                string_dict[sorted_s].append(s)
        list_of_strings = list(string_dict.values())
        return list_of_strings
