class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def insertMerged(intervals, new_interval):
    merged = []
    i = 0
    while i<len(intervals) and intervals[i].end < new_interval.start:
        merged.append(intervals[i])
        i +=1
    while i<len(intervals) and intervals[i].start < new_interval.end:
        new_interval.start = min(new_interval.start, intervals[i].start)
        new_interval.end = max(new_interval.end, intervals[i].end)
        i += 1
    merged.append(new_interval)
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged

if __name__ == '__main__':
    intervals = [Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)]
    new_interval = Interval(4, 9)
    result = insertMerged(intervals, new_interval)
    for interval in result:
        print(interval.start, interval.end)
