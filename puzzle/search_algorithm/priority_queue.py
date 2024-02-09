import numpy as np


class MinHeap:
    def __init__(self):
        self.contents = []
        self.capacity = 0
        self.size = 0
        
    def __getitem__(self, index):
        return self.contents[index]

    def remove_min(self):
        if (self.size < 1):
            return None

        minimum = self.contents[0]
        self.contents[0] = self.contents[self.size-1]
        self.size -= 1

        self.min_heapify(0)

        return minimum
    
    def remove(self, index):
        self.contents.pop(index)
        
        self.capacity -= 1
        self.size -= 1

    def add(self, node):
        self.insert_node(self.size, node)
        self.size += 1

    def parent(self, i):
        return int((i - 1) / 2)

    def child_left(self, i):
        return i*2 + 1

    def child_right(self, i):
        return i*2 + 2
    
    def index(self, state):
        for position, grid in enumerate([n.state for n in self.contents]):
            if np.array_equal(state, grid):
                return position
        
        return None

    def swap_nodes(self, i, j):
        temp = self.contents[i]
        self.contents[i] = self.contents[j]
        self.contents[j] = temp

    def min_heapify(self, i):
        l = self.child_left(i)
        r = self.child_right(i)

        minimum = i

        if l < self.size and self.contents[i].f > self.contents[l].f:
            minimum = l

        if r < self.size and self.contents[minimum].f > self.contents[r].f:
            minimum = r

        if minimum != i:
            self.swap_nodes(i, minimum)
            self.min_heapify(minimum)

    def insert_node(self, i, node):
        if self.capacity == self.size:
            self.contents.append(node)
            self.capacity += 1
        else:
            self.contents[i] = node
        
        while i > 0 and self.contents[self.parent(i)].f > self.contents[i].f:
            self.swap_nodes(i, self.parent(i))
            i = self.parent(i)

    def list_nodes(self):
        return self.contents[:self.size]


class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()
        
    def __getitem__(self, idx):
        return self.heap[idx]

    def index(self, node):
        return self.heap.index(node.state)

    def add(self, node):
        self.heap.add(node)
        
    def remove(self, node):
        self.heap.remove(self.index(node))

    def remove_idx(self, idx):
        self.heap.remove(idx)

    def remove_min(self):
        return self.heap.remove_min()

    @property
    def list_nodes(self):
        return self.heap.list_nodes()
