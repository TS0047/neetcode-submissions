"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        a = sorted(intervals, key= lambda x:x.start)
        rooms = [a[0]]
        for i in a[1:] :
            for k in range(0,len(rooms)):
                if i.start>=rooms[k].end:
                    rooms[k] = i
                    break
            else:
                rooms.append(i) 
        return len(rooms)


            

        