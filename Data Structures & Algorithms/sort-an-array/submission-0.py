class Solution:
    def merge(self, nums: List[int], low : int, mid: int, high : int) -> None:
        temp_list: List[int] = []
        left, right = low, mid+1

        while left <= mid and right <= high:
            if nums[left] <= nums[right]:
                temp_list.append(nums[left])
                left += 1
            else:
                temp_list.append(nums[right])
                right += 1
        
        while left <= mid:
            temp_list.append(nums[left])
            left += 1
        
        while right <= high:
            temp_list.append(nums[right])
            right += 1

        for i in range(low, high+1):
            nums[i] = temp_list[i-low]


    def merge_sort(self, nums: List[int], low : int, high : int) -> None:
        if low == high:
            return
        
        mid = low + (high - low) // 2
        self.merge_sort(nums,low,mid)
        self.merge_sort(nums,mid+1,high)

        self.merge(nums,low,mid,high)

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.merge_sort(nums,0,n-1);

        return nums