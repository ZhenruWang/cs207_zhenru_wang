import copy
from enum import Enum


class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node: 
            return BSTNode(key, val)
        if   key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if   key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val
        
    def _removemin(self,node):
        '''
        It takes a node as an argument. 
        It will return the subtree with the smallest node (the node with the smallest key) removed.
        '''
        if (node.left == None):
            return node.right
        else:
            node.left = self._removemin(node.left)
            node.size = 1 + self._size(node.left) + self._size(node.right)
            return node
    
    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        # TODO: Should return a subtree whose root is <node> but without
        #       the node whose key is <key>
        if not node:
            raise KeyError(f'key not found: {key}')
        
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
                
        else:
        #found key == node.key
            
            #if node has no child, then should return None
            # if node has no left child or no right child
            if not node.right :
                return node.left
            if not node.left:
                return node.right
            # it has both left and right children
            t = copy.deepcopy(node)
            node = self.find_min(t.right)
            node.right = self._removemin(t.right)
            node.left = t.left
            
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def find_min(self,node):
        ''' Return the minimum node in the subtree with root node.
        '''
        if (node.left == None):
            return node
        else:
            return self.find_min(node.left)
        
    @staticmethod
    def _size(node):
        return node.size if node else 0
    
class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        self.tree = tree
        self.type = traversalType

    def __iter__(self):
        self.stack = []
        if self.type == DFSTraversalTypes.INORDER:
            self.inorder(self.tree)
        elif self.type == DFSTraversalTypes.PREORDER:
            self.preorder(self.tree)
        elif self.type == DFSTraversalTypes.POSTORDER:
            self.postorder(self.tree)
        return self
    
    def __next__(self):
        if len(self.stack) != 0:
            res = self.stack.pop(0)
            return res
        else:
            raise StopIteration ('the entire BST has been traversed')
            
    def inorder(self, bst: BSTTable):
        node = bst._root
        def inner(node: BSTNode):
            if node.left:
                inner(node.left)
            if node:
                self.stack.append(node)
            if node.right:
                inner(node.right)
        inner(node)
        
    def preorder(self, bst: BSTTable):
        node = bst._root
        def inner(node: BSTNode):
            if node:
                self.stack.append(node)
            if node.left:
                inner(node.left)
            if node.right:
                inner(node.right)
        inner(node)
        
    def postorder(self, bst: BSTTable):
        node = bst._root
        def inner(node: BSTNode):
            if node.left:
                inner(node.left)
            if node.right:
                inner(node.right)
            if node:
                self.stack.append(node)
        inner(node)
        