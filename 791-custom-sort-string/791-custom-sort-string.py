class Solution:
    '''
    idea is to map order char with index
    if order is abcd
    map :{
    a:0
    b:1
    c:2
    d:3
    }
    
    2. make counter of chars in string s. This will give us how many times particular character is present in the string. if string is bacadab,
    counter = {
    b:2
    a:3,
    c:1
    d:1
    }
    
    now traverse through order and check if it's present in the counter. that means wether the character is present in the string S or not. if yes, check it's occorance count in the counter map and add it to the string that many times
    res_string = char*occurance count form counter
    once we check each and every character in the order and and generate our string builder, 
    now our task is to find the characters in string which are not even listed in the order string. all of them could be pushed to the end by tracking if counter keys are present in order or not.
    
    if not present, then these are not listed in the orders string and we must append them to the end. Remember to append the same count of the non ordered chars too. 
    
    eg: consider the same order as above, ord = abcd
    s = bacadabsiinbadgereg
    counter = {
    b :3
    a: 4
    c: 1
    d: 2
    s:1
    i:2
    n:1
    g:2
    e:2
    r:1
    }
    first string build the ordered chars and later string build the un ordered chars. the count must be the same in both the cases
    result = bbbaaaacdd <-ordered + unordered -> siinggeer 
    res = bbbaaaacddsiinggeer
    
    '''
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
            
            
            
        