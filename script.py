class RingBufferQueue:
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self.data = [None] * capacity
        self.head = 0
        self.tail = 0
        self.count = 0

    def enqueue(self, value: int) -> None:
        if self.is_full():
            print("Предупреждение: очередь переполнена, элемент не добавлен.")
            return

        self.data[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.count += 1

    def dequeue(self) -> int | None:
        if self.is_empty():
            return None

        value = self.data[self.head]
        self.data[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.count -= 1

        return value

    def peek(self) -> int | None:
        if self.is_empty():
            return None
        return self.data[self.head]

    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.capacity

    def size(self) -> int:
        return self.count

    def to_list(self) -> list[int]:
        result = []
        index = self.head
        i = 0

        while i < self.count:
            result.append(self.data[index])
            index = (index + 1) % self.capacity
            i += 1

        return result