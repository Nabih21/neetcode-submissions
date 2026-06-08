class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        seen = set()
        for i in range(len(intervals)-1):
            if intervals[i][1] >=  intervals[i+1][0]:
                intervals[i+1][0] = intervals[i][0]
                if intervals[i][1] >=  intervals[i+1][1]:
                    intervals[i+1][1] = intervals[i][1]
 
        
        print(intervals)

        for i in range(len(intervals) -1, -1 , -1):
            if intervals[i][0] not in seen:
                res.append(intervals[i])
                seen.add(intervals[i][0])
                print(intervals[i])

        return res


        