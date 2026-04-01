class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            sym = ["+", "*", "/", "-"]
            if i not in sym:
                stack.append(int(i))
            elif i == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                total = num1 + num2
                stack.append(total)
             
            elif i == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                total = num2 - num1
                stack.append(total)

            elif i == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                total = num1 * num2
                stack.append(total)
            
            elif i == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                total = int(num2 / num1)
                stack.append(total)

        return stack.pop()