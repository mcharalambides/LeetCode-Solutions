class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1

        i = 1
        last_num = nums[0]
        counter = 1
        k = 0
        while i < len(nums):
            if nums[i] == last_num:
                if counter >= 2:
                    nums[i] = max(nums) + 1
                    k += 1
                counter += 1
            else:
                last_num = nums[i]
                counter = 1
            i = i + 1

        # if nums[-1] == last_num and counter == 2:
        #     nums[-1] = max(nums) + 1
        nums.sort()
        return len(nums) - k
        