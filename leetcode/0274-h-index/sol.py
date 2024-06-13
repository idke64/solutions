class Solution:
    def hIndex(self, citations: List[int]) -> int:
        psum = [0 for _ in range(1001)]
        for i in range(len(citations)):
            psum[citations[i]] += 1
        for i in range(len(psum) - 2, -1, -1):
            psum[i] += psum[i+1]
            if psum[i] >= i:
                return i
        
        return 0
        
            
        