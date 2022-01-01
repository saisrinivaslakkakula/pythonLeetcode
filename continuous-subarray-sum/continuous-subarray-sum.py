class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pref_tracker = {}
        prefSum = 0
        for i,n in enumerate(nums):
            prefSum += n
            rem = prefSum%k
            #print(rem)
            if (rem ==0) and i>=1: return(True) 
            #if rem ==k: pref_tracker[rem] = i
            if rem in pref_tracker:
                #print("Rem in pref Tracker", i-pref_tracker[rem])
                if i - pref_tracker[rem] >1:
                    return(True)
            else:
                pref_tracker[rem] = i
        return(False)
        #print(pref_tracker)
            
        