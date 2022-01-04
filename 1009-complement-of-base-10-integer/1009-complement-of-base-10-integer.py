class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = "{0:b}".format(n)
        print(binary)
        binary = list(binary)
        for i,b in enumerate(binary):
            if b=='0': binary[i] = '1'
            else: binary[i] = '0'
        res = "".join(binary)
        return(int(res,2))
            
                
            
        