class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        from itertools import permutations

        perm = permutations(nums)

        unique_data = [list(x) for x in set(x for x in perm)]

        return unique_data


        