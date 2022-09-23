class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return
        if len(nums) == 1:
            return nums[0]
        
        my_dict = dict.fromkeys(nums,0)
        
        for num in nums:
            my_dict[num] += 1
            
        return [k for k, v in my_dict.items() if v == 1][0]