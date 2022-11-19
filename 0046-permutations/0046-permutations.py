# A Python program to print all 
# permutations using library function 
from itertools import permutations 
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]: 


        perm = permutations(nums)
    
        return [list(x) for x in perm]