class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {} # hash table
        for i, num in enumerate(nums): # look for target - num 
          if target - num in hash:
            return[hash[target-num], i]
          hash[num] = i
