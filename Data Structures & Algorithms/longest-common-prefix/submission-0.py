class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j = min(len(i) for i in strs)
        l = []
        
        for k in range(0, j):                    # outer: positions
            for i in range(1, len(strs)):        # inner: strings
                if strs[i][k] != strs[0][k]:     # compare each string to first
                    return "".join(l)            # return immediately on mismatch
            l.append(strs[0][k])                 # append character if all match
        
        return "".join(l)