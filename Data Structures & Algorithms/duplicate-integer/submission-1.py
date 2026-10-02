class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create set (sets cannot accept duplicates)
        checkSet = set()

        #add each int from the list to the set
        for num in nums:
            checkSet.add(num)

        #check that the sizes match or not for duplicates
        if len(checkSet) == len(nums):
            return False
        else:
            return True
        
            
        