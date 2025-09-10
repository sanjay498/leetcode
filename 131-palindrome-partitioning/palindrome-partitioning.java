class Solution {
    public List<List<String>> partition(String s) {
        char[] ch = s.toCharArray();
        int n = ch.length;

        List<List<String>> ans = new ArrayList<>();
        helper(0, n, new ArrayList<>(), ans, ch);

        return ans;
    }

    void helper(int i, int n, List<String> curr, List<List<String>> ans, char[] ch) {
        if(i == n) {
            ans.add(new ArrayList<>(curr));
            return;
        }

        for(int j=i; j<n; j++) {
            if(isPalindrome(i, j, ch)) {
                curr.add(new String(ch, i, j - i + 1));
                helper(j+1, n, curr, ans, ch);
                curr.remove(curr.size() - 1);
            }
        }
    }

    boolean isPalindrome(int i, int j, char[] ch) {
        while(i < j) {
            if(ch[i] != ch[j]) return false;
            i++;
            j--;
        }

        return true;
    }
}