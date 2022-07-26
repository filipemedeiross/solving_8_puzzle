# Documentation available at tests/informed_search.ipynb


class MinHeap:
    def __init__(self):
        self.contents = []
        self.capacity = 0
        self.size = 0

    def remove_min(self):
        if self.size < 1:
            return None

        minimun = self.contents[0]
        self.contents[0] = self.contents[self.size - 1]
        self.size -= 1

        self.min_heapify(0)

        return minimun

    def add(self, node):
        index = self.size

        if self.capacity == self.size:
            self.contents.append(node)
            self.capacity += 1

        self.insert_node(index, node)
        self.size += 1

    def parent(self, i):
        return int((i - 1) / 2)

    def child_left(self, i):
        return i * 2 + 1

    def child_right(self, i):
        return i * 2 + 2

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
        self.contents[i] = node

        while i > 0 and self.contents[self.parent(i)].f > self.contents[i].f:
            self.swap_nodes(i, self.parent(i))
            i = self.parent(i)


class PriorityQueue:
    def __init__(self):
        self.heap = MinHeap()

    def remove_min(self):
        return self.heap.remove_min()

    def add(self, node):
        self.heap.add(node)
