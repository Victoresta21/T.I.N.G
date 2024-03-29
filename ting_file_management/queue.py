class Queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if (len(self.data) == 0):
            return None
        else:
            return self.data.pop(0)

    def search(self, index):
        if (index < 0):
            raise IndexError
        else:
            return self.data[index]
