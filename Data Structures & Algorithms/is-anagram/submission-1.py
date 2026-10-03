class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #how to do this? sort the string? compare to see if equal?
        sortedS = "".join(sorted(s))
        sortedT = "".join(sorted(t))
        #compare the new sorted strings
        if sortedS == sortedT:
            return True
        return False
        