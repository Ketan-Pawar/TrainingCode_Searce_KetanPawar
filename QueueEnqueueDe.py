# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 13:29:59 2022

@author: Sanjay
"""

class Queue():
    
    def __init__(self):
        self.queue = []
    
    # Add an Element
    def enqueue(self, item):
        self.queue.append(item)
        
    # Remove an Element
    def dequeue(self, item):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    
    # Display an element
    def display(self):
        print(self.queue)
        
    def size(self):
        return len(self.queue)
    
q = Queue()
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)

q.display()

q.dequeue()     

print("After removing an element: ", q.display())   
    
        
        