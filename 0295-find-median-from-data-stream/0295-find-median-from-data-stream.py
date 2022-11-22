class MedianFinder:

    def __init__(self):
        self.nums = []
        self.median = 0
        

    def addNum(self, num: int) -> None:
        if len(self.nums) == 0:
            self.nums.append(num)
            self.findMedian()
            return
        
        if num == self.median:
            self.nums.insert(len(self.nums)//2,num)
            self.findMedian()
            return
        elif num < self.median:
            for i in range(0,len(self.nums)//2 + 1):
                if self.nums[i] >= num:
                    self.nums.insert(i,num)
                    self.findMedian()
                    return
        else:
            for i in range(len(self.nums)//2, len(self.nums)):
                if self.nums[i] >= num:
                    self.nums.insert(i,num)
                    self.findMedian()
                    return
            
                
        if self.nums[0] > num:
            self.nums.insert(0,num)
        else:
            self.nums.append(num)   
        self.findMedian()
        

    def findMedian(self) -> float:
        if len(self.nums) == 1:
            self.median = self.nums[0]
            return self.median
        
        if len(self.nums) % 2 != 0:
            self.median = self.nums[len(self.nums)//2]
            return self.median
        
        self.median = (self.nums[len(self.nums)//2 - 1] + self.nums[len(self.nums)//2]) / 2
        return self.median
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()