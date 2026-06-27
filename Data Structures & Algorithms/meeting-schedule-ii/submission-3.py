class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        a = sorted(intervals, key= lambda x:x.start)
        rooms = [a[0].end]
        for i in a[1:] :
            for k in range(0,len(rooms)):
                if i.start>=rooms[k]:
                    rooms[k] = i.end
                    break
            else:
                rooms.append(i.end) 
        return len(rooms)


            

        