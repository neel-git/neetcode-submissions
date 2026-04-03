class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        prefSum = 0
        count = 0

        for num in nums:
            prefSum += num
            remove = prefSum-k
            count += mp[remove]
            mp[prefSum] += 1
        
        return count