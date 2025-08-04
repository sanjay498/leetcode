class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        s = s.replaceAll("[^a-z0-9]", ""); 

        String sv = "";
        for (int i = s.length() - 1; i >= 0; i--) {
            sv += s.charAt(i); 
        }

        for (int i = 0; i < s.length(); i++) {
            if (sv.charAt(i) != s.charAt(i)) {
                return false;
            }
        }

        return true;
    }
}
