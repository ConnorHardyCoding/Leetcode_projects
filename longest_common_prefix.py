class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        string = ""
        answer = ""
        for num in range(1000):
            try:
                for i in strs:
                    try:
                        string += i[num]
                    except:
                        return answer
                if string == string[0] * len(string):
                    answer += string[0]
                    string = ""
                    
                else:
                    return answer
            except:
                return ""
    
sol = Solution()
print(sol.longestCommonPrefix("a"))