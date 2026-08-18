class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        res = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        pairs = res[0:k]
        keys = [i for i, v in pairs]
        return keys