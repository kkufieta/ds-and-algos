import heapq

class KthLargest:

    def __init__(self, nums, k):
        self.min_heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, num):
        heap_size = lambda: len(self.min_heap)

        if heap_size() < self.k or num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)

        if heap_size() > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
    
    def peek(self):
        return self.min_heap[0]
