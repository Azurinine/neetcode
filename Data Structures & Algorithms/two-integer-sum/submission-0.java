class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap <Integer, Integer> complement = new HashMap<>();
        int [] res = new int [2];

        for (int i = 0; i < nums.length; i++) {
            int currInt = nums[i];
            if (complement.containsKey(target - currInt)) {
                res[0] = complement.get(target - currInt);
                res[1] = i;
                break;
            }
            complement.put(currInt, i);
        }
        return res;
    }
}
