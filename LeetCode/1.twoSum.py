class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = dict()
        for idx, value in enumerate(nums):
            other_value = target - value
            if other_value in m:
                return [m[other_value], idx]
            m[value] = idx
        return None


