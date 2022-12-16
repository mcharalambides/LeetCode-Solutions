from sortedcontainers import SortedList
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        subarray = SortedList(nums[0:k])
        current = subarray[-1]
        result.append(current)
        for i in range(k, len(nums)):

            subarray.remove(nums[i-k])
            subarray.add(nums[i])
            result.append(subarray[-1])

        return result
        