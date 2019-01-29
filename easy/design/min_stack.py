"""solved, medium"""


class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum
    element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        current_min = (x if not self.data or self.data[len(self.data)-1].min > x
                       else self.data[len(self.data)-1].min)

        self.data.append(self._Node(x, current_min))

    def pop(self):
        """
        :rtype: void
        """
        if self.data:
            del self.data[len(self.data)-1]

    def top(self):
        """
        :rtype: int
        """
        return None if not self.data else self.data[len(self.data)-1].val

    def getMin(self):
        """
        :rtype: int
        """
        return None if not self.data else self.data[len(self.data)-1].min
    
    
    class _Node():
        def __init__(self, val, min):
            self.val = val
            self.min = min


if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.getMin() == -3
    min_stack.pop()
    assert min_stack.top() == 0
    assert min_stack.getMin() == -2

    min_stack = MinStack()
    min_stack.push(-1)
    min_stack.top()
    min_stack.getMin()