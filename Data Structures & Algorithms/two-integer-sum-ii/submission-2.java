class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i = 0;
        int j = numbers.length - 1;

        do {
            int sum = numbers[i] + numbers[j];
            if (sum == target) {
                break;
            }
            if (sum < target) {
                i++;
            } else { 
                j--;
            }
        } while (true);

        return new int[] {i + 1, j + 1};
    }
}
