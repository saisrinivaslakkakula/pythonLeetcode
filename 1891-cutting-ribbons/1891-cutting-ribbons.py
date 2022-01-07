class Solution(object):
    def maxLength(self, ribbons, k):
        """
        :type ribbons: List[int]
        :type k: int
        :rtype: int
        """
        low = 1
        high = max(ribbons)+1
        while low < high:
            mid = ((high+low)) //2
            if sum(rib //  mid for rib in ribbons) < k:
                high = mid 
            else:
                low = mid + 1
        return(low-1)
                    
                
        