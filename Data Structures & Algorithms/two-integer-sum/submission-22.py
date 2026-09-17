class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices={}
        #go thru list once and mark position
        for i,n in enumerate(nums):
            indices[n] = i
        #go thru list again, figure out what num u need to hit target
        for i,n in enumerate(nums):
            difference = target - n
            if difference in indices and indices[difference] != i:
                return [i, indices[difference]]
        return []