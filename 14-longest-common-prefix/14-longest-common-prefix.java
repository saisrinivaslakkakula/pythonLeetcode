class Solution {
    public int LCA(String s1,String s2){
        int i=0;
        while((i<s1.length()) && (i<s2.length())){
            if(s1.charAt(i)!= s2.charAt(i))
                break;
            i++;
        }
        return(i);
    }
    public String longestCommonPrefix(String[] strs) {
        int i=1;
        if (strs.length ==1){
            return(strs[0]);
        }
        int len=Integer.MAX_VALUE;
        while(i<strs.length){
            int Common = this.LCA(strs[i],strs[i-1]);
            if (Common<len){
                len = Common;
            }
            i++;
        }
        //System.out.println(len);
        if(strs[0].length()>0)
            return (strs[0].substring(0,len));
        else{
            return("");
        }
    }
}