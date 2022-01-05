class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_map = {}
        for i,o in enumerate(order):
            order_map[o] = i
        counter = Counter(s)
        s_in = ""
        s_notin = ""
        
        for o in order:
            if o in counter:
                s_in += o*counter[o]
        for char in counter:
            if char not in order_map:
                s_in += char*counter[char]
        return(s_in)
            
            
            
        