class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        c=str(x)
        b=c[::-1]
        
        if c == b:
            return True
        else:
            return False