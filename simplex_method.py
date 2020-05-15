#53. Maximum Subarray
#Given an integer array nums, find the contiguous subarray (containing at least 
#one number) which has the largest sum and return its sum.
class Solution(object):
    def maxSubArray(self, nums):
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
        return max(dp)
nums = [-2,1,-3,7,-2,2,1,-5,4,1,21]
ob1 = Solution()
print(ob1.maxSubArray(nums)) 