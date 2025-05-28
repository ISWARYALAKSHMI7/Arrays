class Solution(object):
  def twoSum(self, nums, target):
    numMap = {}
    for i, num in enumerate(nums):
        numMap[num] = i
    for i, num in enumerate(nums):
        complement = target - num
        if complement in numMap and numMap[complement] != i:
            return [i, numMap[complement]]
    return []