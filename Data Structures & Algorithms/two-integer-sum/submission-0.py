class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        w1, w2 = 0, 1

        while w1 < len(nums):
            if nums[w1] + nums[w2] == target:
                return [w1, w2]

            if w2 == len(nums) - 1:
                w1 += 1
                w2 = w1 + 1
            else:
                w2 += 1