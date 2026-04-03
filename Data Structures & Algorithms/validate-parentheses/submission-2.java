class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack <> ();
        Map<Character, Character> mapping = Map.of(
            ')', '(',
            ']', '[',
            '}', '{'
            );


        char[] charArr = s.toCharArray();
        for (char c : charArr) {
            Character compliment = mapping.get(c);
            if (compliment == null) {
                stack.push(c);
            } else if (stack.size() == 0 || stack.pop() != compliment) {
                return false;
            }
            
        }

        return stack.size() == 0;
    }
}
