class Solution:
    def is_possible(self, piles: List[int], h: int,k: int) -> bool:
        curr_h = 0
        for i in range(len(piles)):
            curr_h += piles[i]//k
            if piles[i]%k != 0:
                curr_h += 1
        
        return curr_h <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = -1

        while low <= high:
            mid = low + (high - low)//2
            if self.is_possible(piles,h,mid):
                ans = mid;
                high = mid - 1
            else:
                low = mid + 1
            
        return ans