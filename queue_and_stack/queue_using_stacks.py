class MyQueue(object):


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.s1.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.s1:
            self.s2.append(self.s1[-1])
            self.s1.pop(-1)
        to_pop = self.s2[-1]
        self.s2.pop(-1)

        while self.s2:
            self.s1.append(self.s2[-1])
            self.s2.pop(-1)

        return to_pop




    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while self.s1:
            self.s2.append(self.s1[-1])
            self.s1.pop(-1)
        first_elmn = self.s2[-1]
        while self.s2:
            self.s1.append(self.s2[-1])
            self.s2.pop(-1)
        return first_elmn


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.s1

if __name__ == '__main__':

    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    param_3 = obj.peek()
    param_2 = obj.pop()
    param_4 = obj.empty()

    print(param_2)
    print(param_3)
    print(param_4)
