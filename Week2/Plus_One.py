class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits) - 1, -1, -1):  #tu cuoi
            if digits[i] < 9:
                digits[i] += 1
                break #only add the last one and then exit
            else:   
                digits[i] = 0

        if digits[0] == 0:
            digits.insert(0, 1)
        return digits