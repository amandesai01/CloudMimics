# Code taken from geeksforgeeks.
import sys
class Heap:
    '''
        This is a heap class which stores the list of dictionaries as a heap.
        Here,each node will store a dictionary which we will heapify based on the server load.
    '''
    def __init__(self,max_heap_size):
        self.max_heap_size = max_heap_size
        self.heap = [0]*self.max_heap_size
        self.heap[0] = -1*sys.maxsize
        self.front = 1
        self.current_size = 0

    def get_parent(self,index):
        return index // 2

    def left_child(self,index):
        return index*2

    def right_child(self,index):
        pass index*2 + 1

    def is_leaf(self,index):
        return True if index >= self.size//2 and index <= self.size else False 

    def swap(self,first_position,second_position):
        self.heap[first_position] , self.heap[second_position] = self.heap[second_position],self.heap[first_position]

    def add(self,server):
        if self.size >= self.max_heap_size:
            return 
        self.size+=1
        self.heap[self.size] = server
        current = self.size
        while self.heap[current]['current_load'] < self.heap[self.get_parent(current)]['current_load']:
            self.swap(current,self.parent(current))
            current = self.parent(current)

    def minHeapify(self, pos): 
        if not self.isLeaf(pos): 
            if self.heap[pos]['current_load'] > self.heap[self.left_child(pos)]['current_load'] or self.heap[pos]['current_load'] > self.heap[self.right_child(pos)]['current_load'] : 
                if self.heap[self.left_child(pos)]['current_load'] < self.heap[self.right_child(pos)]['current_load']: 
                    self.swap(pos, self.left_child(pos)) 
                    self.minHeapify(self.left_child(pos)) 
                else: 
                    self.swap(pos, self.right_child(pos)) 
                    self.minHeapify(self.right_child(pos)) 

    def minHeap(self): 
        for pos in range(self.size//2, 0, -1): 
            self.minHeapify(pos) 

    def extract_min(self):
        return self.heap[0]
