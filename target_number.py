class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1
        
sol = Solution()
print(sol.search([1, 2, 9], 4))
