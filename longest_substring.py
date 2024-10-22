class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ""
        count = 0
        char_count = []
        for char in s:
            if char not in longest:
                longest += char
                if len(longest) > count:
                    count = len(longest)
            else:
                if char not in char_count:
                    if longest[-1] == char:
                        longest = char
                    else:
                        longest = longest[longest.index(char)+1:] + char
                        if len(longest) > count:
                            count = len(longest)
                        char_count.append(char)
                elif char in char_count:
                    longest = longest[longest.index(char)+1:] + char
                    char_count.remove(char)
        return count
    
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcab"))