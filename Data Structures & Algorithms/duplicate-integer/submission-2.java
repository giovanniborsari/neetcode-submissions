class Solution {
    public boolean hasDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++){
            for (int k = i + 1; k < nums.length; k++){
                if (nums[k] == nums[i]){ 
                    return true;
                    }
            }
        } 
        return false;
    }
}