class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map <String, List<String> > result = new HashMap <> ();

        for (String curr: strs) {
            int [] count = new int [26];
            for (int i = 0; i < curr.length(); i++) {
                count[curr.charAt(i) - 'a']++;
            }
            String key = Arrays.toString(count);

            result.putIfAbsent(key, new ArrayList<String> ());
            result.get(key).add(curr);
        }

        return new ArrayList<>(result.values());
    }
}
