class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append((x, min(x, self.getMin())))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else float('inf')


if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    minStack = MinStack()

    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    # return -3
    minStack.pop()
    print(minStack.top())
    # return 0
    print(minStack.getMin())
    # return -2
