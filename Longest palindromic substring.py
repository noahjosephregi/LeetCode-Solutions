class Solution(object):
    def expand(self,s,i,j):
        while i>=0 and j<len(s) and s[i]==s[j]:
            i-=1
            j+=1
        return s[i+1:j]
    def longestPalindrome(self, s):
        ans=''
        for i in range(len(s)):
            ans=max(ans,self.expand(s,i,i), self.expand(s,i,i+1), key=len)
        return ans
            
    