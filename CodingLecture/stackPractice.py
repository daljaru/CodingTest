

testList = []


class Stack(list):
    push = list.append

    def peek(self):
        return self[-1]


testStack = Stack(testList)

if testStack:
    print(1)