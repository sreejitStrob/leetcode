from typing import List


class Solution:
    def maxSubArray(nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0 :
                curSum = 0
            curSum += n
            maxSub = max(maxSub,curSum)
        return maxSub






maxSubArray = Solution();
print(Solution.maxSubArray([-2,-1,0,-4,-1,-2,-1,-5,-1]))