class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Selection sort
        n : int = len(nums)
        for i in range(n-1):
            mini_idx : int = i
            for j in range(i+1,n):
                if nums[j] < nums[mini_idx]:
                    mini_idx = j
                
            nums[i],nums[mini_idx] = nums[mini_idx],nums[i]

        return nums
