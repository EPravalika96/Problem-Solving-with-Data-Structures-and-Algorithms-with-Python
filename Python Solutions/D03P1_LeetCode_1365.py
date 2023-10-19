# Python3 code coming soon


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        d1={}
        sorted_nums = sorted(nums)
        for i in range(0,len(nums)):
            if sorted_nums[i] not in d1:
                d1[sorted_nums[i]] = i
        for i in nums:
            res.append(d1[i])
        return res
