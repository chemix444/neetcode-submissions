class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        get = seen.get

        for i, num in enumerate(nums):
            match = get(target - num)
            if match is not None:
                return [match, i]
            seen[num] = i
