class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> nums = new Stack<>();

        for (String s : tokens) {
            switch (s) {
                case "+":
                    nums.push(nums.pop() + nums.pop());
                    break;
                case "-":
                    nums.push(-nums.pop() + nums.pop());
                    break;
                case "*":
                    nums.push(nums.pop() * nums.pop());
                    break;
                case "/":
                    int divisor = nums.pop();
                    int numerator = nums.pop();
                    nums.push(numerator / divisor);
                    break;
                default: 
                    nums.push(Integer.valueOf(s));
            }
        }
        return nums.pop();
    }
}
