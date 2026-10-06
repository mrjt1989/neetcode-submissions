class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #if I am reading this right(had to use hints to get the problem)
        #we need to return the k number of most frequent (most number of the int) in an array
        #say we have [1,2,2,3,3,3] k=2. this is [2,3] because they have the top 2 most 
        #number of ints 2 of 2 and 3 of 3
        #so the solution is using buckets based on frequency?
        #in a set there can be no duplicates right?

        #dictionary hashmap
        intCountDict = {}
        for num in nums:
            if num not in intCountDict:
                intCountDict[num] = 1
            else:
                intCountDict[num] = intCountDict[num] + 1

        #create a list of lists
        intCountList = []
        for key, value in intCountDict.items():
            intCountList.append([key, value])

        #sort with lambda function which i appreciate google's help
        sortedIntCountList = sorted(intCountList, key=lambda x:x[1])
        #return list
        topK = []
        for i in range(k):
            tempList = sortedIntCountList.pop()
            topK.append(tempList[0])

        return topK


        #EVERYTHING BELOW FAILED BECAUSE I DID NOT ACCOUNT FOR DICTIONARIES REQUIRING UNIQUE KEYS SO NUMBERS WITH THE SAME COUNT WERE BEING OVERWRITTEN
        # #make a dictionary(hashmap)

        
        # #


        
        # #swap the key and values
        # countDict = {}
        # #also make a list of the count numbers
        # count = []
        # for key, value in seen.items():
        #     countDict[value] = key
        #     count.append(value)
        # count.sort(reverse=True)
        # print("here are the count dictionary and list of the counts reversed")
        # print(countDict)
        # print(count)
        
        # #create the output list
        # freqInts = []
        # for i in range(k):
        #     freqCount = count[i]
        #     freqInts.append(countDict[freqCount])
        # return freqInts

        


        
            
                
