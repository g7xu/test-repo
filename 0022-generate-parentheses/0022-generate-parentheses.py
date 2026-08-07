class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        def go(cur, op, cl):
            if len(cur) == 2 * n:
                out.append("".join(cur)); return
            if op < n:
                go(cur + ["("], op + 1, cl)
            if cl < op:
                go(cur + [")"], op, cl + 1)
        go([], 0, 0)
        return out
