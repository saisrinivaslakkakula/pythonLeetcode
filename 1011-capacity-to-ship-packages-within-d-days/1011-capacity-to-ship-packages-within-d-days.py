class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # VERY IMPORTANT - READ THE NOTES CAREFULLY
        # First find the lower and upper limits. which are max(weights) and sum (weights)
        low = max(weights)
        high = sum(weights)
        while low<high:
            mid = (low+high)//2
            #print(mid)
            wt_accumulator = 0
            cur_days = 1
            for w in weights:
                if wt_accumulator+w > mid:
                    cur_days +=1
                    wt_accumulator = 0
                wt_accumulator += w
            if cur_days > days:     # this means my shipping days increased;  which in turn means I need to increase the minimum capacity of the ship. to do this I will increase mid towards right.
                low = mid+1
            else:  #This means it took me less days to ship all the packages with the min weight selected. so it's time I should decrease my weight.
                high = mid
        return low
    '''

    
    '''
                
            
        