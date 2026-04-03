class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        HashMap <Character, Integer> firstWord = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            Character currChar = s.charAt(i);
            if (firstWord.containsKey(currChar)) {
                firstWord.put(currChar, firstWord.get(currChar) + 1);
            }
            else {
                firstWord.put(currChar, 1);
            }
        }

        for (int i = 0; i < t.length(); i++) {
            Character currChar = t.charAt(i);
            if(!firstWord.containsKey(currChar)) {
                return false;
            }

            firstWord.put(currChar, firstWord.get(currChar) - 1);
            if (firstWord.get(currChar) < 0) return false;
        }
        return true;
    }
}
