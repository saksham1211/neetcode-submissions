class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        sorted_list = ["".join(sorted(s)) for s in strs]
        dic={}
        for i, s in enumerate(sorted_list):
            if s in dic:
                dic[s].append(strs[i])

            else:
                dic[s]=[strs[i]]

        for key, value in dic.items():
            res.append(value)

        return res