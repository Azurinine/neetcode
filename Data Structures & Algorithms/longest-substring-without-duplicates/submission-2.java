class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() == 1) {
            return 1;
        }
        int res = 0;
        int l = 0, r = 0;

        Map<Character, Integer> hash = new HashMap<>();
        while (r < s.length()) {
            char curr = s.charAt(r);
            Integer pos = hash.get(curr);
            hash.put(curr, r);

            if (pos != null) {
                res = Math.max(res, r - l);
                if (pos >= l) {
                    l = pos + 1;
                }
            }
            r++;
        }

        return Math.max(res, r - l);
    }
}
