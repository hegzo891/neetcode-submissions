class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
            set<int> arr;
            for(int i = 0; i < nums.size(); i++){
                arr.insert(nums[i]);
            }
    if(nums.size() == arr.size())           
            return false;
    return true;
    }
};