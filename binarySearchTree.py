class TreeNode:
    """
    Represents a node in a binary search tree.

    Attributes:
        key (int): The key or value of the node.
        left (TreeNode): The left child node.
        right (TreeNode): The right child node.
    """

    def __init__(self, key):
        """
        Initializes the tree node with the given key.

        Args:
            key (int): The key or value of the node.
        """
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        """
        Returns a string representation of the node.

        Returns:
            str: The string representation of the key.
        """
        return str(self.key)

class BinarySearchTree:
    """
    Represents a binary search tree.

    Attributes:
        root (TreeNode): The root node of the binary search tree.
    """

    def __init__(self):
        """
        Initializes the binary search tree with an empty root.
        """
        self.root = None

    def _insert(self, node, key):
        """
        Recursively inserts a key into the tree.

        Args:
            node (TreeNode): The current node in the tree.
            key (int): The key to be inserted.

        Returns:
            TreeNode: The new node after insertion.
        """
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def insert(self, key):
        """
        Inserts a key into the binary search tree.

        Args:
            key (int): The key to be inserted.
        """
        self.root = self._insert(self.root, key)
        
    def _search(self, node, key):
        """
        Recursively searches for a key in the tree.

        Args:
            node (TreeNode): The current node in the tree.
            key (int): The key to search for.

        Returns:
            TreeNode: The node with the key, or None if not found.
        """
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def search(self, key):
        """
        Searches for a key in the binary search tree.

        Args:
            key (int): The key to search for.

        Returns:
            TreeNode: The node with the key, or None if not found.
        """
        return self._search(self.root, key)

    def _delete(self, node, key):
        """
        Recursively deletes a key from the tree.

        Args:
            node (TreeNode): The current node in the tree.
            key (int): The key to delete.

        Returns:
            TreeNode: The new node after deletion.
        """
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key) 
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left   
            
            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)   
        
        return node

    def delete(self, key):
        """
        Deletes a key from the binary search tree.

        Args:
            key (int): The key to delete.
        """
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        """
        Finds the minimum value in the tree.

        Args:
            node (TreeNode): The current node in the tree.

        Returns:
            int: The minimum key value.
        """
        while node.left is not None:
            node = node.left
        return node.key

    def _inorder_traversal(self, node, result):
        """
        Recursively performs an inorder traversal of the tree.

        Args:
            node (TreeNode): The current node in the tree.
            result (list): The list to store the traversal result.
        """
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        """
        Performs an inorder traversal of the binary search tree.

        Returns:
            list: The list of keys in inorder sequence.
        """
        result = []
        self._inorder_traversal(self.root, result)
        return result

# Example usage
bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

# Insert nodes into the binary search tree
for node in nodes:
    bst.insert(node)

# Search for a node
print('Search for 80:', bst.search(80))

# Inorder traversal of the tree
print("Inorder traversal:", bst.inorder_traversal())

# Delete a node from the tree
bst.delete(40)

# Search for a node after deletion
print("Search for 40:", bst.search(40))

# Inorder traversal after deleting a node
print('Inorder traversal after deleting 40:', bst.inorder_traversal())
