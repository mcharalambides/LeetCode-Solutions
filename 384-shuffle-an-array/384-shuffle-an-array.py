class Solution:

    def __init__(self, nums: List[int]):
        self.state = nums
        self.init = list(nums)
        

    def reset(self) -> List[int]:
        self.state = self.init
        self.init = list(self.init)
        return self.state

    def shuffle(self) -> List[int]:
        random.shuffle(self.state)
        return self.state


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()