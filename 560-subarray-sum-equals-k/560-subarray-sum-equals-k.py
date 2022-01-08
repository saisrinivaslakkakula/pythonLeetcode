class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # VERY IMPORTANT PROBLEM - READ THE NOTES CAREFULLY
        count = 0
        pref_sum = 0
        pref_sum_map = {}
        for num in nums:
            # pref_sum + num is current prefix sum 
            cur_pref = pref_sum+num
            #print(cur_pref)
            if cur_pref ==k: 
                #print(cur_pref, "is equal to",k )
                count+=1
            key = cur_pref - k
            #print("key",key)
            if key in pref_sum_map:
                count += pref_sum_map[key]
                #print("k- found")
                #count+=1
            if cur_pref not in pref_sum_map:
                pref_sum_map[cur_pref] = 1
            else:
                cur_count = pref_sum_map[cur_pref]
                cur_count +=1
                pref_sum_map[cur_pref] = cur_count
            #print(pref_sum_map)
            pref_sum = cur_pref
        return count
        
            
            
            
        