from collections import deque

testDeque = deque()


class Queue(list):
    push = list.append

    def get(self):
        self.pop(0)

    def peek(self):
        return self[0]


testList = [1,2,3,4,5]
testQueue = Queue(testList)

testQueue.get()
print(testQueue.peek())
print(testQueue)