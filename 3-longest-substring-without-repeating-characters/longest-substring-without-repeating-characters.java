import java.util.HashMap;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        String sub = "";
        int len = s.length();
        int maxlen = 0;

        for (int i = 0; i < len; i++) {
            if (sub.indexOf(s.charAt(i)) == -1) {
                sub += s.charAt(i); 
                maxlen = Math.max(maxlen, sub.length()); 
            } else {
                sub = sub.substring(sub.indexOf(s.charAt(i)) + 1) + s.charAt(i);
            }
        }

        return maxlen;
    }
}
