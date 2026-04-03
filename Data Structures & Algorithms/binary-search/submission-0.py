class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n-1
        ans = -1

        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                ans = mid
                return ans
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
            
        return ans