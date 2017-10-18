#2017/10/17

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        cur_min = self.getMin()

        if cur_min is None:
            cur_min = x

        self.stack = self.stack + [(x, min(x, cur_min))]

    def pop(self):
        """
        :rtype: void
        """
        self.stack = self.stack[0:-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][1]



        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()

temp = MinStack()
temp.getMin()
temp.push(0)
temp.pop()