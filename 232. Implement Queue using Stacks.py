# -*- coding: utf-8 -*-
# @Time    : 2017/11/5 10:29
# @Author  : Jiahao Yang
# @Email   : yangjh39@uw.edu


class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.que = self.que + [x]

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        pe = self.que[0]
        self.que.remove(pe)
        return pe

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.que[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.que) == 0



        # Your MyQueue object will be instantiated and called as such:
        # obj = MyQueue()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.peek()
        # param_4 = obj.empty()