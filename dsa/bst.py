import queue
from typing import Type 

class BinarySearchTree:

    def __init__(self, value):
        # only one parameter for our root node
        self.root = self.Node(value)


    class Node:
        # initially, both child nodes will be empty
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

            '''
            6
            3    8
            2 5 

            '''
    def bfs(self):

        if not self.root:
            return None;

        '''
        pseudocode for BFS

        enqueue the root node, then do the loop

        loop goes like:
        while (queue not empty):
        1. deque the queue
        2. process it
        3. enqueue the childs to the queue (assuming children exist, if children don't exist, don't do anything)
        ''' 
        

        # use Queue object
        q = queue.Queue()
        # each value in the queue is a Node object, not just the value. pretty useless if you store just the value (since you lose all the context)
        q.put(self.root)
        print(f'Alright, so the root node is {self.root.value}')
        while (not q.empty()):
            current_node = q.get()
            print(current_node.value)

            if (current_node.left):
                q.put(current_node.left)

            if (current_node.right):
                q.put(current_node.right)
            

def Main():
    tree = BinarySearchTree(5)
    print(f'The root node should be {tree.root.value}')
    tree.root.left = tree.Node(3)
    tree.root.right = tree.Node(6)
    tree.root.left.left = tree.Node(2)
    tree.root.left.right = tree.Node(4)
    tree.root.right.right = tree.Node(13)
    tree.root.right.left = tree.Node(10)
    tree.bfs()


if __name__ == "__main__":
    Main()

