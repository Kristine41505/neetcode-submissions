class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #first lets create a hashmap where we can store nums in
        seen={}
        for num in nums:
            if num in seen:
                return True
            seen[num]= True
        return False
        