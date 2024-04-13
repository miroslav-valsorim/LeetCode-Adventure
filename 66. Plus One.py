class Solution(object):
    def plusOne(self, digits):
        string_num = ''
        int_num = 0
        for n in digits:
            string_num += str(n)
            int_num = int(string_num)

        int_num += 1
        string_num = str(int_num)

        end_list = [int(s) for s in string_num]

        return end_list


solution = Solution()
s = solution.plusOne([1, 2, 3])
print(s)
