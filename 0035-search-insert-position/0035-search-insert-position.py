class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums)
        mid = 0

        while low <= high:

            mid = (high + low) // 2
            
            if mid >= len(nums):
                return len(nums)

            # If x is greater, ignore left half
            if nums[mid] < target:
                low = mid + 1

            # If x is smaller, ignore right half
            elif nums[mid] > target:
                high = mid - 1

            # means x is present at mid
            else:
                return mid

                # If we reach here, then the element was not present
        if nums[mid] < target:
            return mid + 1
        else:
            return mid