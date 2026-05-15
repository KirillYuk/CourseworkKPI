class BiQueue:
    def __init__(self):
        self.queue = []
        self.counter = 0
        
    def enqueue(self, item, priority):
        self.queue.append((self.counter, priority, item))
        self.counter += 1

    def _select(self, mode):
        if len(self.queue) == 0:
            return None
        
        if mode == 'highest':
            return max(self.queue, key=lambda x: x[1])
            
        elif mode == 'lowest':
            return min(self.queue, key=lambda x: x[1])
            
        elif mode == 'oldest':
            return min(self.queue, key=lambda x: x[0])
        
        elif mode == 'newest':
            return max(self.queue, key=lambda x: x[0])
        
        raise ValueError("Unknown mode: " + mode)

    def dequeue(self, mode):
        item = self._select(mode)
        if item is None:
            return None
        self.queue.remove(item)
        return item[2]
    
    def peek(self, mode):
        item = self._select(mode)
        if item is None:
            return None
        return item[2]
