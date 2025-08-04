class Solution {
    public void reverseString(char[] s) {
        int  r=0,l=s.length -1;
        while(r<l){
            char temp=s[l];
            s[l]=s[r];
            s[r]=temp;
            l--;
            r++;
        }System.out.print(s);


        
    }
}