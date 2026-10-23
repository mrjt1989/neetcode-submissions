class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #I think I get it
        #seems like i might need to double for loop it (nest it up
        #that was wrong haha

        #go right
        leftList = [1]
        listLength = len(nums)
        index = 0
        for num in nums:
            if index == 0:
                index += 1
            else:
                product = leftList[index - 1] * nums[index - 1]
                leftList.append(product)
                index += 1
        
        rightList = [1]
        
        for i in range(listLength - 1):
            index -= 1
            rightList.append(nums[index] * rightList[i])
            
        
        #final list creation (convoluted I know)
        finalList = []
        for i in range(listLength):
            product = leftList[i] * rightList[listLength - 1 - i]
            finalList.append(product)

        return finalList


        
