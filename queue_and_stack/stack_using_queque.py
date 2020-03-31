class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        q_size = len(self.q)
        for i in range(q_size-1):
            self.q.append(self.q[0])
            self.q.pop(0)
        to_pop = self.q[0]
        self.q.pop(0)
        return to_pop


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        q_size = len(self.q)
        for i in range(q_size):
            self.q.append(self.q[0])
            last_elem = self.q[0]
            self.q.pop(0)
        return last_elem

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.q

if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_3 = obj.top()
    param_2 = obj.pop()
    param_4 = obj.empty()

    print(param_2)
    print(param_3)
    print(param_4)