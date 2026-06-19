class MinStack:

    def __init__(self):
        self.stack = []
        self.pointer = -1
        

    def push(self, val: int) -> None:
        self.pointer +=1
        self.stack.append(val)

    def pop(self) -> None:
        if(self.pointer>-1):
            self.pointer-=1
            self.stack.pop()

    def top(self) -> int:
        if(self.pointer>-1):
            return self.stack[self.pointer]

    def getMin(self) -> int:
        if(self.pointer>-1):
            return min(self.stack[:self.pointer+1])
        
