class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = sorted(s)
        t1 = sorted(t)
        s2 = ''.join(s1)
        t2 = ''.join(t1)

        if s2 == t2:
            return True
        else:
            return False
        
