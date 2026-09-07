class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0

        checking_sign = True
        sign = 1
        for char in s.strip():
            
            if checking_sign:
                if char == '-':
                    sign = -1
                    
                checking_sign = False
                
                if char in ['-', '+']:
                    continue

                
                

            if not char.isdigit():
                break

            res = res * 10
            res += int(char)

        res = sign * res
        res = max(res, -2 ** 31)
        res = min(res, 2 ** 31 - 1)

        return res
                    

            
