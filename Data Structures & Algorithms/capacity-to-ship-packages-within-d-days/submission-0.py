class Solution:
    def is_possible(self, weights: List[int], days: int, cap: int) -> bool:
        curr_day = 1
        curr_cap = 0
        for w in weights:
            curr_cap += w
            if curr_cap > cap:
                curr_day += 1
                curr_cap = w
            
        return curr_day <= days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = 0
        for w in weights:
            high += w
        ans = low
        
        while low <= high:
            mid = low + (high - low) // 2
            if self.is_possible(weights, days, mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
            
        return ans