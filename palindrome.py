class Solution:
    def isPalindrome(self, x: int) -> bool:
        xx = str(x)
        return xx == xx[::-1]


sol = Solution()
print(sol.isPalindrome(1000))