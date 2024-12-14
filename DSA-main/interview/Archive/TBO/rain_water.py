class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=[]
        sum=0
        height_so_far=height[n-1]
        left.append(height[0])
        for i in range(1,n):
            left.append(max(height[i],left[i-1]))
        for i in range(n-2,0,-1):
            height_so_far=max(height_so_far, height[i+1])
            val=min(height_so_far, left[i-1])-height[i]
            if val>0:
                sum=sum+val
        return sum


        



        