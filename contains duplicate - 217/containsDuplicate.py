from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        
        for i,num in enumerate(nums):
            if num in hashMap:
                return True
            
            hashMap[num] = i
        
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        hashMap = set()
        
        for i,num in enumerate(nums):
            if num in hashMap:
                return True
            
            hashMap.add(num)
        
        return False
        