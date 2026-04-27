class BiQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0
        
    def enqueue(self, item, priority):
        self.queue.append((self.counter, priority, item))
        self.counter += 1

    def dequeue(self, mode):
        if len(self.queue) == 0:
            return None
        
        if mode == 'highest':
            item = max(self.queue, key=lambda x: x[1])
        elif mode == 'lowest':
            item = min(self.queue, key=lambda x: x[1])

        self.queue.remove(item)
        return item[2]