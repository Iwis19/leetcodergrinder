// Last updated: 3/6/2026, 9:31:41 PM
class Solution {
    public int[] twoSum(int[] nums, int target) {

        int l = nums.length;
        boolean found = false;
        int[] output;

        
        for(int i = 0; i < l; i++){
            for(int j = 0; j < l; j++){
                if(nums[i] + nums[j] == target && i != j){
                    found = true;
                }
                if(found == true){
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{0,0};
    }
}