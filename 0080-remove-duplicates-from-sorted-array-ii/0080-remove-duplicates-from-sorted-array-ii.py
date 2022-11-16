class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1

        i = 1
        last_num = nums[0]
        counter = 1
        k = 0
        dummy_num = max(nums)
        while i < len(nums):
            if nums[i] == last_num:
                if counter >= 2:
                    nums[i] = dummy_num
                    k += 1
                counter += 1
            else:
                last_num = nums[i]
                counter = 1
            i = i + 1
        
        
        for i in range(0,k):
            nums.remove(dummy_num)
            nums.append(0)
        return len(nums) - k
        