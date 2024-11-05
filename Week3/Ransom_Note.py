class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_count = {}
        for i in magazine:
            magazine_count[i] = magazine_count.get(i,0) + 1
        for each in ransomNote:
            if magazine_count.get(each) > 0:
                magazine_count[each] -=1
            else:
                return False
        return True 



        