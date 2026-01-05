class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        lst=set()
        maxlen=0
        for right in range(len(s)):
            while s[right] in lst:

                lst.remove(s[left])
                left=left+1
            lst.add(s[right])

            maxlen=max(maxlen,right-left+1)
        
        return maxlen
            