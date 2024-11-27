class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        n = len(nums)
        lo, hi = min(nums), max(nums)
        B = defaultdict(list)
        for num in nums:
            if num == hi:
                ind=n-1
            else:
                ind=(abs(num-lo)*(n-1))//(hi-lo)
            B[ind].append(num)   
        buckets=[]
        for i in range(n):
            if B[i]:
                buckets.append((min(B[i]),max(B[i])))
        ans=0
        for i in range(1,len(buckets)):
            ans=max(ans,abs(buckets[i-1][-1]-buckets[i][0]))
        return ans     
        