class Solution {
    public int lengthOfLongestSubstring(String s) {        
        int res = 0, l = 0, r = 0;

        Map<Character, Integer> hash = new HashMap<>();
        for (; r < s.length(); r++) {
            char curr = s.charAt(r);
            Integer pos = hash.get(curr);
            hash.put(curr, r);

            if (pos != null) {
                res = Math.max(res, r - l);
                if (pos >= l) {
                    l = pos + 1;
                }
            }
        }

        return Math.max(res, r - l);
    }
}
