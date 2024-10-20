from random import choice
class Solution:
    def climb_stairs(self, n: int) -> int:
        count = 0
        test_no = 0
        num = 0
        sum_list = []
        while True:
            num_list = []
            while True:
                one_or_two = choice([1, 2])
                num += one_or_two
                num_list.append(one_or_two)
                if test_no == 10000:
                    break
                if num == n:
                    if num_list not in sum_list:
                        sum_list.append(num_list)
                        test_no = 0
                    else:
                        test_no += 1
                    num_list =[]
                    num = 0
                if num > n:
                    num_list = []
                    num = 0
            count = len(sum_list)
            if test_no == 10000:
                    break

        print(count)

sol = Solution()
sol.climb_stairs(16)