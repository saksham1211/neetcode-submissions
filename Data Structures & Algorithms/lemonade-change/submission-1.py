class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        currency = defaultdict(int)

        for b in bills:
            if b==5:
                currency[5]+=1

            elif b==10:
                if currency[5]>=1:
                    currency[5]-=1
                    currency[10]+=1

                else:
                    return False

            elif b==20:
                if currency[5]>=3:
                    currency[5]-=3
                    
                elif (currency[5]>=1 and currency[10]>=1):
                    currency[5]-=1
                    currency[10]-=1

                else:
                    return False


        return True