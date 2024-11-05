class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        new_dict = {}
        for i in s:
            new_dict[i] = new_dict.get(i,0) + 1

        for index, letter in enumerate(s): #index truoc leter sau
            if new_dict[letter] == 1:
                return index
        return -1

        