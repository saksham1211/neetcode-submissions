class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}

        for c in s:
            dic_s[c] = 1 + dic_s.get(c, 0)

        for c in t:
            dic_t[c]=1+dic_t.get(c, 0)

        return dic_s==dic_t