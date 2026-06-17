class Solution {
    public boolean hasDuplicate(int[] nums) {
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++){
            if((i+1) < nums.length){
               int k = i+1;
                if (nums[i] == nums[k]){ 
                    return true;
                    }
            }
        }
        return false;
        } 
        
    }
