class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for char in range(len(s)-1, -1, -1):
            if s[char].lower() in "abcdefghijklmnopqrstuvwxyz":
                count += 1
            elif s[char] == " " and count != 0:
                break
        return count