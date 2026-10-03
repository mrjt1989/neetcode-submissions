class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #this will be me replicating the solution from the solution video
        #create a set (not a dictionary) 
        checkSet = set()
        #iterate through the list
        for num in nums:
            #check if the number is already in the set
            if num in checkSet:
                #if so it has a duplicate
                return True
            #if not continue
            checkSet.add(num)
        #return false if for loop completes
        return False

#old solution
#create dictionary (hashmap) for seen ints
        # seen = {}
        # #loop through the list
        # for num in nums:
        #     #check if the number is in the list
        #     if num in seen:
        #         return True
        #     else:
        #         #add it to the dictionary
        #         seen[num] = 1
        # #return the false if no matches found
        # return False
        #I realize that i do not need a dictionary to do this. but refreshing the memory on dictionaries is nice. maybe could have used a set? I think the solutions are to convert the list to a dictionary then compare the length.
        