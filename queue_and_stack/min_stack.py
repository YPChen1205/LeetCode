class MinStack(object):
    def __init__(self):

        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = 2147483647  # biggest int

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.stack:
            self.min = x
        elif self.min > x:
            self.min = x

        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        to_pop = self.stack[-1]
        self.stack.pop()

        return to_pop

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3)
    print(param_4)
