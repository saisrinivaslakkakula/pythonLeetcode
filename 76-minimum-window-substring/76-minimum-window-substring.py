import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        if s == t: 
            return s
        l = r =0
        t_map = Counter(t)
        required = len(t_map)
        formed = 0
        s_map = dict()
        min_window_len = float('inf')
        min_window_l = 0
        min_window_r = 0
        while r<len(s):
            curr_char = s[r]
            if curr_char not in s_map and curr_char in t_map: 
                s_map[curr_char] = 1
            elif curr_char in s_map and curr_char in t_map: 
                
                cur_char_count = s_map[curr_char]
                cur_char_count+=1
                s_map[curr_char] = cur_char_count
            if curr_char in t_map and s_map[curr_char] == t_map[curr_char]:
                formed+=1
            while formed == required and l<=r:
                #print(formed,required,l,r)
                curr_char_l = s[l]
                if r-l+1 < min_window_len:
                    min_window_len =  r-l+1
                    min_window_l = l
                    min_window_r = r
                if curr_char_l in s_map:
                    #print("Curr_char," ,curr_char, "in S_map")
                    curr_char_count = s_map[curr_char_l]
                    #print(curr_char_count)
                    curr_char_count -=1
                    s_map[curr_char_l] = curr_char_count
                    #print(curr_char_count)
                #print(s_map)
                if curr_char_l in t_map and s_map[curr_char_l] < t_map[curr_char_l]:
                    formed -=1
                l +=1
            
            r+=1
        print(min_window_l,min_window_r,min_window_len)
        if min_window_len == float('inf'): return ""
        else:
            return(s[min_window_l:min_window_r+1])
        
        
        
        
        
        