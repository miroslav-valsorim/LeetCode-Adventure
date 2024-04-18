class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()

        if words:
            return len(words[-1])
        else:
            return 0

    #  return len(s.strip().split(' ')[:-1][0])   doesn't strip all extra spaces


solution = Solution()
s = solution.lengthOfLastWord('   fly me   to   the moon  ')
print(s)
