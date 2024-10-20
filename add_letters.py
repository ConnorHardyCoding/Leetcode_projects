class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newstring = ""
        count = 0
        if len(word1) >= len(word2):
            for letter in word1:
                newstring += letter
                try:
                    newstring += word2[count]
                except:
                    break
                count += 1
            return newstring + word1[count+1:]
        else:
            for letter in word1:
                newstring += letter
                try:
                    newstring += word2[count]
                except:
                    break
                count += 1
            return newstring + word2[count:]

sol = Solution()

print(sol.mergeAlternately("abcd", "pgrrvfsvsv"))