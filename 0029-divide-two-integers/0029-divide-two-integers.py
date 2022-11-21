class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if (divisor > 0 and dividend > 0) or (divisor < 0 and dividend < 0) :
            multiplier = 1
        else:
            multiplier = -1
    
        ans = 0 # the quotient is intialized
        
        a = dividend
        b = divisor
        
        a = abs(a) # making sure both the numbers
        b = abs(b) # are positive

        for i in range(31,-1,-1): # starting our loop

            if b << i <= a  : # checking if b multiplied by 2**i is <= a 
                a -= b << i   # subtracting b << i from a
                ans += 1 << i # adding 2 power i to the answer

        # and finally checking if the output should be negative and returning it
        if ans * multiplier > 2**31 - 1:
            return 2**31 - 1
        elif ans * multiplier < -2**31:
            return -2**31
        else:
            return ans * multiplier