class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans,st=0,-1
        freq=Counter()
        for end in range(len(nums)):
            freq[nums[end]] += 1
            while freq[nums[end]] > k:
                st+=1
                freq[nums[st]]-=1
            ans=max(ans,end-st)
        return ans
        