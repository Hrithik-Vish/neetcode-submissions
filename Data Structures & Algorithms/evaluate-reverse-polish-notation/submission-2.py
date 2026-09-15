class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk_1 = []

        for val in tokens:

            if val == "+":
                v2 = stk_1.pop()
                v1 = stk_1.pop()
                stk_1.append(v1 + v2)
            elif val == "-":
                v2 = stk_1.pop()
                v1 = stk_1.pop()
                stk_1.append(v1 - v2)
            elif val == "*":
                v2 = stk_1.pop()
                v1 = stk_1.pop()
                stk_1.append(v1 * v2)
            elif val == "/":
                v2 = stk_1.pop()
                v1 = stk_1.pop()
                stk_1.append(int(v1 / v2))
            else:
                stk_1.append(int(val))
        return stk_1[0]