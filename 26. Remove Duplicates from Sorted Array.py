from collections import OrderedDict


class Solution(object):
    def removeDuplicates(self, nums):

        # res = []
        # [res.append(x) for x in nums if x not in res]
        #
        # return res

        # return len(set(nums))

        nums[:] = OrderedDict.fromkeys(nums)
        return len(nums)


solution = Solution()
s = solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
print(s)
