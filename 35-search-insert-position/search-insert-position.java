class Solution {
    public int searchInsert(int[] nums, int target) {
        int a=nums.length;
        int s=-1;
        for(int i=0;i<a;i++){
            if(nums[i]==target){
                s=i;
                return s;
                
            }if(nums[i]>target){
                return i;
            }
        
        }return a;
        }
        
        }
        
        