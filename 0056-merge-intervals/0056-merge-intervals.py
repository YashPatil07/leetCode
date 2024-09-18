class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged_list = []
        intervals.sort(key=lambda x:x[0])
        for i in range(len(intervals)):
            if not merged_list or merged_list[-1][1] < intervals[i][0]:
                merged_list.append(intervals[i])
            else:
                merged_list[-1][1] = max(merged_list[-1][1],intervals[i][1])
        
        return merged_list