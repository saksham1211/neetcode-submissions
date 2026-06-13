class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        company = [(c, p) for c, p in zip(capital, profits)]

        heapq.heapify(company)
        maxHeap=[]
        for _ in range(k):

            while company and company[0][0]<=w:
                c, p = heapq.heappop(company)
                heapq.heappush(maxHeap, -p)

            if maxHeap:
                w+=-heapq.heappop(maxHeap)

        return w