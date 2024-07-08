class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # for i in range(0,m):
        #     if nums2[0] < nums1[i]:
        #         nums1[i:i] = [nums2.pop(0)]
        # return nums1
        
        
        if n>0:
            for i in range(m,m+n):
                nums1[i] = nums2[i-m]
            nums1.sort()
