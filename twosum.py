class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        count_1 = 0
        for number in nums:
            if number <= target:
                count_2 = 0
                for n in nums:
                    if number + n == target and count_1 != count_2:
                        return [count_1, count_2]
                    count_2 += 1
            count_1 +=1
        
    

sol = Solution()
print(sol.twoSum([0, 3, 4, 0], 0))