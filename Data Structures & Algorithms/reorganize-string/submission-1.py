class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = {}
        for c in s:
            if c in cnt:
                cnt[c] += 1
            else:
                cnt[c] = 1
        
        maxHeap = [[-freq, letter] for letter, freq in cnt.items()]
        heapq.heapify(maxHeap)

        temp = None
        result = ""
        while maxHeap:
            i, char = heapq.heappop(maxHeap)
            result += char
            i += 1

            if temp and temp[0] != 0:
                heapq.heappush(maxHeap, temp)
                temp = None

            temp = [i, char]
        
        print(result)
        if temp and temp[0] < 0:
            return ""

        return result