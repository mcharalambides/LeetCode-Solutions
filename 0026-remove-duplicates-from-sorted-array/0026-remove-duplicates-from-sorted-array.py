class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1
        finalNums = set(nums)
        k = len(finalNums)
        i=1
        dummy_num = max(nums)+1
        last_num = nums[0]
        while i<len(nums)-1:
            if nums[i] == last_num:
                nums[i] = dummy_num
            else:
                last_num = nums[i]
            i=i+1
        if nums[-1] == nums[-2]:
            nums[-1] = dummy_num
        nums.sort()
        return k
        