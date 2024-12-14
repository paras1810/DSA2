import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes) -> int:
        if n==1: return 1
        hp = heapq(primes)
        if n==2: return heapq.heappop()
        res = 0
        for i in range(2, n):
            res = heapq.heappop()
            heapq.heappush(2*res)
        return res 
        
    
n=12
primes = [2,7,13,19]
print(Solution.nthSuperUglyNumber(n, primes))