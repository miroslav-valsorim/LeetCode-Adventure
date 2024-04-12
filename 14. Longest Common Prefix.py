class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)

        for i in range(min_len):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[0][i]:
                    return strs[0][:i]

        return strs[0][:min_len]


solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
print(solution.longestCommonPrefix(["dog", "racecar", "car"]))