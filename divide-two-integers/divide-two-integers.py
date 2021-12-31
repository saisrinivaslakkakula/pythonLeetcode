class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quo = 0
        quoTrack = 0
        positive = True
        if dividend <0 or divisor <0: positive = False
        if dividend <0 and divisor <0: positive = True
        #else: positive: False
        if dividend < 0: dividend = -dividend
        if divisor<0 : divisor = -divisor
        constdivisor = divisor
        while dividend >= divisor:
            if quo ==0: quo =1
            else: quo += quo
            quoTrack += quo
            dividend -= divisor
            divisor += divisor
            if divisor > dividend: 
                divisor = constdivisor
                quo = 0
        if not positive:  
            quoTrack = - quoTrack
            if quoTrack < pow(-2,31): quoTrack = pow(-2,31)
        else:
            if quoTrack > pow(2,31)-1: quoTrack = pow(2,31)-1
        return quoTrack
        
            
            