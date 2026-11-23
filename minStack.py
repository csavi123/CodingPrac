class MinStack:

    def __init__(self):
        self.s1=[]
        self.minStack=[]

    def push(self, val: int) -> None:
        self.s1.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.s1.pop()
        if val == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        val= self.s1[-1]
        return val

    def getMin(self) -> int:
        val = self.minStack[-1]
        return val
        

if __name__ == "__main__":
    s = MinStack()
    s.push(5)
    s.push(1)
    s.push(8)
    s.pop()
    print(s.getMin())
    print(s.top())

    #with Time Complexity O(1) and space complexity is O(n)