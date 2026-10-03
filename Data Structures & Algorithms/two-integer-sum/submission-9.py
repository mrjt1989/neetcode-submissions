class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #so we need to output the indices of the two ints that combined equal the target
        #brute force would be a double loop grab an index and compare it to all then try the next if the first did not work
        #iterate through the list via indices
        for i in range(len(nums)):
            #grab the index
            firstNumIndex = i
            #remove the number
            firstNum = nums.pop(i)
            #iterate through the new list without the first number
            for j in range(len(nums)):
                #add the numbers
                if (firstNum + nums[j]) == target:
                    #if they equal the sum then return it
                    return [i, j + 1]
            #re-add the number back in where it was to not break the for loop as I was doing
            nums.insert(i, firstNum)
    #NOTES: this is very inefficient 
            

            