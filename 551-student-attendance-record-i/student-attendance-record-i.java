class Solution {
    public boolean checkRecord(String s) {
        int absents = 0; 
        int lateStreak = 0; 
        
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            
            if (ch == 'A') {
                absents++;
                if (absents > 1) return false;
            }
            
            if (ch == 'L') {
                lateStreak++;
                if (lateStreak >= 3) return false;
            } else {
                lateStreak = 0;
            }
        }
        
        return true;
    }
}
