class Solution:

    def encode(self, strs: List[str]) -> str:
        #going with hint 3 again (not sure how to emplement blank strings)
        #go through the words and at the length + delimiter
        #combine into a string
        encodedStr = ''
        
        for word in strs:
            wordLenDelimiter = str(len(word)) + '#'
            encodedStr += wordLenDelimiter + word
        print(encodedStr)
        return encodedStr


            
    def decode(self, s: str) -> List[str]:
        #now to decode this shizzzz
        #here is the list
        decodedList = []
        #now how to do a loop
        lenS = len(s)
        decoded = 0
        while lenS > decoded:

            delimIndex = s.index('#')
            print(f"index of #: {delimIndex}")
            stringLen = int(s[:delimIndex])
            print(f"string length: {stringLen}")
            
            decodedWord = s[(delimIndex + 1):(delimIndex + stringLen + 1)]
            print(f"Decoded Word: {decodedWord}")
            decodedList.append(decodedWord)
            s = s[(delimIndex + stringLen + 1):]
            decoded += (delimIndex + stringLen + 1)
            

        return decodedList


        #I believed the problem what for case 30 something that it was getting caught on the false delimiter in the string but it is actually the double digit size of the string.
        #I need to figure that out.
        #so what we need to do is grab the whole int for the size of the string when the only one is the char right next to the delimiter
        





