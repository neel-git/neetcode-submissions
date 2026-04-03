class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefProd = [0]*n
        suffProd = [0]*n
        prefProd[0] = 1
        suffProd[n-1] = 1

        for i in range(1,n):
            prefProd[i] = prefProd[i-1]*nums[i-1]
        
        for i in range(n-2,-1,-1):
            suffProd[i] = suffProd[i+1]*nums[i+1]
        
        ans = []
        for i in range(n):
            ans.append(prefProd[i]*suffProd[i])

        return ans

