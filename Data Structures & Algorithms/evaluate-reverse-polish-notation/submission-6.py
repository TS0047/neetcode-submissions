class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for i in tokens:
            if i.isdigit() or (i.startswith('-') and len(i)>1):
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                
                match i:
                    case '+': 
                        stack.append(a + b)
                    case '-': 
                        stack.append(a - b)
                    case '*': 
                        stack.append(a * b)
                    case '/': 
                        stack.append(int(a / b))
                        
        return stack.pop()
