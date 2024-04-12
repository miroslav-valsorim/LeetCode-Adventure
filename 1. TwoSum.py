class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums) - 1):
            num_to_sum = i
            for j in range(i + 1, len(nums)):
                if nums[num_to_sum] + nums[j] == target:
                    # print([num_to_sum, j])
                    return [num_to_sum, j]


solution = Solution()

print(solution.twoSum([2, 7, 11, 15], 9))
