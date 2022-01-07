class Solution:
    def operate(self,stack,num_d,op):
        #print("sb:",stack,num_d,op)
        if op == '+':
            stack.append(num_d)
        elif op == '-':
            stack.append(-num_d)
        elif op =='*':
            stack[-1] = stack[-1]*num_d
        elif op =='/':
            if stack[-1]<0: 
                res = abs(stack[-1])//num_d
                stack[-1] = -res
            else:stack[-1] = stack[-1]//num_d
        #print("sa:",stack)
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        op = '+'
        stack = []
        s = s.replace(" ","")
        num = ""
        num_d = 0
        for ch in s:
            if ch.isdigit():
                num+=ch
            else:
                if len(num)>0:num_d = int(num)
                self.operate(stack,num_d,op)  
                #print(num_d,op)
                num = ""
                op=ch
        self.operate(stack,int(num),op)
        return(sum(stack))
        