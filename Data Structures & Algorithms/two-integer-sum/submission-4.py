class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            dif = target - nums[i]
            start_index = i + 1
            try:
                dif_index = nums.index(dif, start_index)
                return [i, dif_index]
            except ValueError:
                None
        return None