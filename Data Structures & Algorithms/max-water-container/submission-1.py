class Solution:
    def maxArea(self, heights: List[int]) -> int:
        out=0
        x,y = 0,len(heights)-1
        while(x!=y):
            out = max(out,(y-x)*min(heights[x],heights[y]))
            if(heights[x]<heights[y]):
                x+=1
            else:
                y-=1
        return out


        