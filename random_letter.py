class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = {}
        t_dict = {}
        for letter in s:
            if letter not in s_dict:
                s_dict[letter] = 1
            else:
                s_dict[letter] += 1
        
        for letter in t:
            if letter not in t_dict:
                t_dict[letter] = 1
            else:
                t_dict[letter] += 1

        for item in t_dict:
            if item not in s_dict or t_dict[item] > s_dict[item]:
                print(item)
        


sol = Solution()

sol.findTheDifference("monkey", "monkeyx")