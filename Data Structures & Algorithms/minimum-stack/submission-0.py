class node:
    def __init__(self, val):
        self.nextNode = None
        self.prevNode = None
        self.minVal = val
        self.val = val


class MinStack:

    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val: int) -> None:
        newNode = node(val)
        if self.tail:
            self.tail.next = newNode
            newNode.prevNode = self.tail
            newNode.minVal = min(self.tail.minVal, val)
        else:
            self.head = newNode
        self.tail = newNode

    def pop(self) -> None:
        if not self.tail:
            return

        self.tail = self.tail.prevNode
        if self.tail:
            self.tail.nextNode = None
        else:
            self.head = None

    def top(self) -> int:
        if self.tail:
            return self.tail.val
        return None

    def getMin(self) -> int:
        if self.tail:
            return self.tail.minVal
        return None
