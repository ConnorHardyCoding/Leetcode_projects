class Solution:
    def isValid(self, s: str) -> bool:
        order = ""
        for char in s:
            try:
                if char in ["(", "[", "{"]:
                    order += char
                elif char == ")":

                    if order[-1] == "(":
                        order = order[:-1]
                    else:
                        return False
                elif char == "]":
                    if order[-1] == "[":
                        order = order[:-1]
                    else:
                        return False
                elif char == "}":
                    if order[-1] == "{":
                        order = order[:-1]
                    else:
                        return False
            except:
                return False
        if order == "":
            return True
        else:
            return False
    
sol = Solution()
print(sol.isValid("("))