class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = None
        self.right = None
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
        '''
        _put should return the new root of this subtree. 
        
        node is the root of the subtree into which the 
        key-value pair is to be inserted into.
        
        After the insertion, the root of this subtree may change.
        
        The difference of the input subtree and the returned subtree is that 
        in the returned subtree, a new key-value pair has been inserted. 
        '''
        if node:
            if key == node.key:
                node.val = val
                return self._root
            
            elif key < node.key:
                if node.left == None:
                    new_table = BSTTable()
                    new_table.put(key,val)
                    node.left = new_table
                    node.size += 1
                    return node
                else:
                    node.left.put(key,val)
                    return node
            
            elif key > node.key:
                if node.right == None:
                    new_table = BSTTable()
                    new_table.put(key,val)
                    node.right = new_table
                    node.size += 1
                    return node
                else:
                    node.right.put(key,val)
                    return node
        else:
            #tree is empty
            return BSTNode(key,val)
            

    def _get(self, node, key):
        if node:
            if key == node.key:
                return node.val
            elif key < node.key:
                if node.left:
                    return node.left.get(key)
                else:
                    raise KeyError('No such key found')
                    
            elif key > node.key:
                if node.right:
                    return node.right.get(key)
                else:
                    raise KeyError('No such key found')
        else:
            raise KeyError('No such key found')
            

    @staticmethod
    def _size(node):
        return node.size if node else 0