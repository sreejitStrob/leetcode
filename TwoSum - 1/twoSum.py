from typing import List

class solution:
    def twoSum (self,nums: List[int],target: int) -> List[int]:
        prevMap = {}

        for i,n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        return

twoSum = solution()
print(twoSum.twoSum([3,2,4],6))