class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # with no multiplication/ division or mod
        
        sign = (-1 if dividend < 0 else 1)* (-1 if divisor < 0 else 1)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        dividend = list(str(dividend))
        fin = ''
        remain= ''
        
        while len(dividend) > 0:
            called = dividend.pop(0)
            called_int = int(remain+called)
            tc = 0
            c = 0
            while tc <= called_int:
                c += 1
                tc += divisor
            if c-1 > 0:
                fin += str(c-1)
            else:
                fin+='0'
            remain = str(called_int- (tc-divisor))
        res = int(fin) * sign if fin != '' else 0 
        return max(min(res, 2**31-1), -2**31)