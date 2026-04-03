class Solution {
    public boolean isPalindrome(String s) {
        s= s.toLowerCase();
        char[] str = s.toCharArray();
        int i = 0;
        int j = str.length - 1;

        while (j > i) {
            char l = str[i];
            char r = str[j];
            if (!(l >= 'a' && l <= 'z' || l >= '0' && l <= '9')) {
                i++;
            } else if (!(r >= 'a' && r <= 'z' || r >= '0' && r <= '9')) {
                j--;
            } else if (l != r) {
                return false;
            } else {
                i++;
                j--;
            }
        }
        return true;
    }
}
