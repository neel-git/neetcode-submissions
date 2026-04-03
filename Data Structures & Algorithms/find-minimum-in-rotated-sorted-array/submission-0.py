class Solution:
    def check(self, nums: List[int], mid: int) -> bool:
        if nums[mid] < nums[0]:
            return True

        return False

    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n-1
        ans = nums[0]

        while low <= high:
            mid = low + (high - low) // 2
            if self.check(nums,mid):
                ans = nums[mid]
                high = mid-1
            else:
                low = mid+1
            
        return ans