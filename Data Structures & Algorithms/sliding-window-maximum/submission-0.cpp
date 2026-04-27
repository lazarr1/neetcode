class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {

        std::map<int, int> freqs;
        vector<int> ans;

        for (int i = 0; i < k; i++) {
            int num = nums[i];
            if (freqs.find(num) != freqs.end()) {
                freqs[num]++;
            } else {
                freqs[num] = 1;
            }
        }

        for(int i = k; i < nums.size(); i++) {
            ans.push_back((--freqs.end())->first);

            freqs[nums[i-k]] -= 1;
            int num = nums[i];
            if (freqs.find(num) != freqs.end()) {
                freqs[num]++;
            } else {
                freqs[num] = 1;
            }

            if (freqs[nums[i-k]] == 0){
                freqs.erase(nums[i-k]);
            }
        }
        ans.push_back((--freqs.end())->first);

        return ans;
    }
};
