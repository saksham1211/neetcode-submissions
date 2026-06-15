class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashMap = {}
        for i, char in enumerate(order):
            hashMap[char] = i

        print(hashMap)
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            for j in range(len(w1)):
                if j==len(w2):
                    return False

                if w1[j]!=w2[j]:
                    if hashMap[w1[j]]>hashMap[w2[j]]:
                        return False
                    break
                

        return True