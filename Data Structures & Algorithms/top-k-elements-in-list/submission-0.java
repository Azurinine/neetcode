class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int [] frequency =  new int [2001];
        Map <Integer, List<Integer>> repList = new HashMap<>();
        int result [] = new int [k];
        int found = 0;

        for (int curr : nums) {
            frequency[curr + 1000]++;
        }

        for (int i = 0; i < 2001; i++) {
            int reps = frequency[i];
            repList.putIfAbsent(reps, new ArrayList<Integer>());
            repList.get(reps).add(i - 1000);
        }

        for (int i = nums.length; found < k; i--) {
            if (repList.containsKey(i)) {
                for (int j : repList.get(i)) {
                    result[found++] = j;
                }
            }
        }

        return result;
    }
}
