class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort intervals by start
        intervals.sort(key=lambda x: x[0])

        print(intervals)

        newInt = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= newInt[-1][1]:
                newInt[-1][1] = max(newInt[-1][1], end)
            else:
                newInt.append([start, end])
        
        return newInt