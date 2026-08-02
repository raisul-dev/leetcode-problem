class Solution(object):
    def longestCommonPrefix(self, strs):
        s = sorted(strs)
        first = s[0]
        last = s[-1]
        m = min (strs)
        new = ""
        for i in range (min (len(first),len(last))):
            if first [i] == last[i]:
                new += first[i]
            else :
                break
        return new