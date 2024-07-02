class Stack:
    def __init__(self, size: int) -> None:
        self.array = []
        self.top = -1
        self.size = size
        
    def push(self, item):
        # ~^ This case we will use the concept of size and top to throw the exception, 
        # ~^ since python does not have a concept of fixed sized array
        self.top += 1
        if self.top < self.size:
            self.array.append(item)
        else:
            raise Exception("Stack Overflow exception")
    
    def pop(self):
        self.top -= 1
        if self.top < 0 :
            raise Exception("Stack Underflow exception")
        self.array.pop()
        
    def print(self):
        print(self.array)
        
stack = Stack(3)

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()
# stack.pop()

stack.print()
    