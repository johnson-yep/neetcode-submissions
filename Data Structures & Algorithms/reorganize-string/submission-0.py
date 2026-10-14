class Solution:
    def reorganizeString(self, s: str) -> str:
        #impossible when highest repeat > half len(s)
        n = len(s)
        letters = {}

        for c in s:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
        
        maxHeap = [[-freq, char] for char, freq in letters.items()]
        heapq.heapify(maxHeap)

        result = ""
        prev = None
        while maxHeap or prev:
            if not maxHeap and prev:
                return ""
            freq, char = heapq.heappop(maxHeap)
            result += char
            freq += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if freq != 0:
                prev = [freq, char]

        return result
            
