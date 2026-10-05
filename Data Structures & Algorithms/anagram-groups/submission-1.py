class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a list to hold the lists.
        listOfLists = []
        #maybe make a "unique" string the key in a dictionary and add itself, then any other matches?
        #let us see
        #create dictionary (hashmap)
        seen = {}
        #go through the list
        for word in strs:
            #sort the word and convert to string
            sorted_word = "".join(sorted(word))
            # check if sorted word is in dictionary
            if sorted_word not in seen:
                seen[sorted_word] = []
                seen[sorted_word].append(word)
            
            else:
                seen[sorted_word].append(word)
        #now we should have a dictionary with the key being the anagram with the lists so now I just need to put the lists into the listoflists
        #grab the values of seen and throw them into the list of lists
        for anagramList in seen.values():
            listOfLists.append(anagramList)
        return listOfLists

                
        