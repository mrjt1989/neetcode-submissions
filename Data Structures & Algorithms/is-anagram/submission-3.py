class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #I am doing this one from memory from yesterday from the solution video.
        #will need to compare the sorted strings
        if sorted(s) == sorted(t):
            return True
        return False

        # I just looked at the solution and there is the length check to avoid the sorted function
        