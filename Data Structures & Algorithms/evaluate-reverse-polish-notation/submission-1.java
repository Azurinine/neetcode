class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> nums = new Stack<>();

        for (String s : tokens) {
            if (s.equals("+")) {
                nums.push(nums.pop() + nums.pop());
            } else if (s.equals("-")) {
                nums.push(-nums.pop() + nums.pop());
            } else if (s.equals("*")) {
                nums.push(nums.pop() * nums.pop());
            } else if (s.equals("/")) {
                int divisor = nums.pop();
                int numerator = nums.pop();
                nums.push(numerator / divisor);
            } else {
                nums.push(Integer.valueOf(s));
            }
        }
        return nums.pop();
    }
}
