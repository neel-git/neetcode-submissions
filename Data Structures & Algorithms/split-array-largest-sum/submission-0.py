class Solution:
    def is_valid(self, nums:List[int], mid: int, k: int) -> bool:
        count = 1
        curr_sum = 0

        for num in nums:
            curr_sum += num
            if curr_sum > mid:
                count += 1
                curr_sum = num
                if count > k:
                    return False
        
        return True

    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = 0
        for num in nums:
            high += num
        
        ans = low

        while low <= high:
            mid = low + (high - low)//2
            if self.is_valid(nums,mid,k):
                ans = mid;
                high = mid - 1
            else:
                low = mid + 1
            
        return ans