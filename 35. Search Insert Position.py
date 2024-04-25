class Solution(object):
    def searchInsert(self, nums, target):
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            mid_point = (begin + end) // 2
            mid_num = nums[mid_point]

            if target == mid_num:
                return mid_point

            if target > mid_num:
                begin = mid_point + 1
            else:
                end = mid_point - 1

        return begin


nums1 = [1, 3, 5, 6]
target1 = 5
solution_one = Solution()
s = solution_one.searchInsert(nums1, target1)
print(s)

nums2 = [1, 3, 5, 6]
target2 = 2
solution_two = Solution()
s_two = solution_two.searchInsert(nums2, target2)
print(s_two)


nums3 = [1, 3, 5, 6]
target3 = 7
solution_three = Solution()
s_three = solution_three.searchInsert(nums3, target3)
print(s_three)


