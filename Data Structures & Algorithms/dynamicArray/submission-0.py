class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        if capacity > 0:
            self.array = [0] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = n
        self.size += 1

    def popback(self) -> int:
        pop = self.array[self.size - 1]
        self.size -= 1
        return pop

    def resize(self) -> None:
        oldCap = self.capacity
        self.capacity *= 2
        tempArray = self.array
        self.array = [0] * self.capacity
        for i in range(oldCap):
            self.array[i] = tempArray[i]


    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
