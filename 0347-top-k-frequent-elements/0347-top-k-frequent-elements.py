class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_words = dict.fromkeys(nums,0)

        for x in nums:
            unique_words[x]+=1
        
        unique_words = dict(sorted(unique_words.items(), key=lambda item: item[1],reverse=True))

        return list(unique_words.keys())[0:k]