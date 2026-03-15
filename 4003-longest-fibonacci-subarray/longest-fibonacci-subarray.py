class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        if(n<=2):
            return n
        currlen=2
        maxlen=2
        for i in range(2,n):
            if nums[i]==nums[i-1]+nums[i-2]:
                currlen+=1
            else:
                currlen=2
            maxlen=max(maxlen,currlen)
        return maxlen
        