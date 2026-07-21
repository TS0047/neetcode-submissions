class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def rec(cur, open, close):
            if len(cur) == 2*n:
                ans.append(cur)
                return
            if open < n:
                rec(cur+'(', open+1, close)
            if close < open:
                rec(cur+')', open, close+1)
        rec('', 0, 0)
        return ans