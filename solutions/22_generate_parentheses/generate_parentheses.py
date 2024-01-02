from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if(n==1):
            return ["()"]
        else:
            result = []
            previous = self.generateParenthesis(n-1)
            for e in previous:
                result.append("()"+e)
                result.append("("+e+")")
                result.append(e+"()")
            return list(set(result))
        
solution = Solution()
print(len(solution.generateParenthesis(5)))