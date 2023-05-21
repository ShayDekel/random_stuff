
"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

	@type key: int or None
	@param key: key of your node
	@type value: any
	@param value: data of your node
	"""

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0

    """returns the key

	@rtype: int or None
	@returns: the key of self, None if the node is virtual
	"""

    def get_key(self):
        return self.key

    """returns the value

	@rtype: any
	@returns: the value of self, None if the node is virtual
	"""

    def get_value(self):
        return self.value

    """returns the left child
	@rtype: AVLNode
	@returns: the left child of self, None if there is no left child (if self is virtual)
	"""

    def get_left(self):
        return self.left

    """returns the right child

	@rtype: AVLNode
	@returns: the right child of self, None if there is no right child (if self is virtual)
	"""

    def get_right(self):
        return self.right

    """returns the parent 

	@rtype: AVLNode
	@returns: the parent of self, None if there is no parent
	"""

    def get_parent(self):
        return self.parent

    """returns the height

	@rtype: int
	@returns: the height of self, -1 if the node is virtual
	"""

    def get_height(self):
        return self.height

    """returns the size of the subtree

	@rtype: int
	@returns: the size of the subtree of self, 0 if the node is virtual
	"""

    def get_size(self):
        return self.size

    """sets key

	@type key: int or None
	@param key: key
	"""

    def set_key(self, key):
        self.key = key

    """sets value

	@type value: any
	@param value: data
	"""

    def set_value(self, value):
        self.value = value

    """sets left child

	@type node: AVLNode
	@param node: a node
	"""

    def set_left(self, node):
        self.left = node

    """sets right child

	@type node: AVLNode
	@param node: a node
	"""

    def set_right(self, node):
        self.right = node

    """sets parent

	@type node: AVLNode
	@param node: a node
	"""

    def set_parent(self, node):
        self.parent = node

    """sets the height of the node

	@type h: int
	@param h: the height
	"""

    def set_height(self, h):
        self.height = h

    """sets the size of node

	@type s: int
	@param s: the size
	"""

    def set_size(self, s):
        self.size = s

    """returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""

    def is_real_node(self):
        return self.height > -1

    """ Update the height of the node

        @returns: None
        """
    
    def update_height(self):
        self.set_height(max(self.left.get_height(), self.right.get_height()) + 1)

    """Update the size of the node

        @returns: None
        """
    
    def update_size(self):
        self.set_size(self.left.get_size() + self.right.get_size() + 1)

    """Update both the height and the size of the node

        @returns: None
        """
    
    def update_height_and_size(self):
        self.update_height()
        self.update_size()

    """Turn the node into a leaf (make both childs virtual nodes)

        @returns: None
        """
    
    def make_leaf(self):
        self.left = virtualNode
        self.right = virtualNode
        self.height = 0
        self.size = 1

    """Check if the node is a leaf

        @rtype: bool
        @returns: True if the node is leaf, False otherwise
        """
    
    def is_leaf(self):
        return self.height == 0

    """Return true if the node has only one child and it's his left child

        @rtype: bool
        @returns: True if only child is left child, False otherwise
        """
    
    def is_only_one_child_left(self):
        return self.left != virtualNode and self.right == virtualNode

    """Return true if the node has only one child and it's his right child

        @rtype: bool
        @returns: True if only child is right child, False otherwise
        """
    
    def is_only_one_child_right(self):
        return self.left == virtualNode and self.right != virtualNode

    """Calculate the node's balance factor

        @rtype: int
        @returns: the balance factor of the node
        """
    
    def get_balance_factor(self):
        return self.left.get_height() - self.right.get_height()

    """Return "right" if node is right child of its parent
        Return "left" if node is left child of its parent
        Return "root" if node has no parent

        @rtype: string
        @returns: "right" if node is right child, "left" if node is left child, "root" otherwise
        """

    def get_direction(self):
        parent = self.get_parent()
        if (parent == None):
            return "root"
        if (self == parent.get_left()):
            return "left"
        elif (self == parent.get_right()):
            return "right"

    """" Returns the successor of node
        
        @rtype = int or None
        @returns: the successor of node, None if biggest in tree
        """
    
    def successor(self):
        temp_node = self

        if (temp_node.get_right() != virtualNode):
            temp_node = temp_node.get_right()
            while (temp_node.get_left() != virtualNode):
                temp_node = temp_node.get_left()
            return temp_node
        else:
            temp_node_parent = temp_node.get_parent()
            while (temp_node_parent != None and temp_node_parent.get_right() == temp_node):
                temp_node = temp_node_parent
                temp_node_parent = temp_node.get_parent()
            return temp_node_parent

    """Disconnects the node from it's childs
    
        @returns: None
        """
    
    def disconnect(self):
        left = self.get_left()
        left.set_parent(None)
        self.set_left(virtualNode)

        right = self.get_right()
        right.set_parent(None)
        self.set_right(virtualNode)

virtualNode = AVLNode(None, None)


"""
A class implementing an AVL tree.
"""


class AVLTree(object):
    """
	Constructor, you are allowed to add more fields.

	"""

    def __init__(self):
        self.root = None

    # add your fields here

    """searches for a node in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: node corresponding to key.
	"""

    def search(self, key):
        temp_node = self.root

        while (temp_node != virtualNode):
            if (temp_node.get_key() == key):
                return temp_node
            elif (temp_node.get_key() < key):
                temp_node = temp_node.get_right()
            else:
                temp_node = temp_node.get_left()

        return None

    """inserts val at position i in the dictionary

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def insert(self, key, val):

        BF_cnt = 0

        if (self.root == None or self.root == virtualNode):
            return self.insert_to_empty_tree(key, val)

        """ Regular insert and set the parent of the inserted node """
        parent = self.regular_insert(key, val)

        while (parent != None):
            prev_height = parent.get_height()
            parent.update_height_and_size()
            bf = parent.get_balance_factor()
            if (abs(bf) < 2 and parent.get_height() == prev_height):
                break
            elif (abs(bf) < 2 and parent.get_height() != prev_height):
                BF_cnt += 1
                parent = parent.get_parent()
            elif (abs(bf) == 2):
                BF_cnt += self.rotate(parent, bf)
                break

        """" Continue to go up to the root to update the height and size of nodes """
        BF_cnt += self.continue_to_update(parent)

        return BF_cnt
    
    """Continue to go up to the root to update the height and size of nodes

        @type node: AVLNode
        @param node: the parent of the "AVL offender" after the insertion
        @rtype int
        @returns: Number of height changes made to nodes
        """
    
    def continue_to_update(self, node):
        cnt = 0
        while (node != None):
            prev_height = node.get_height()
            node.update_height_and_size()
            if (prev_height != node.get_height()):
                cnt += 1
            node = node.get_parent()

        return cnt

    """Insert a new node with key and val as the root of an empty tree

        @type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: any
	@param val: the value of the item
        @rtype: int
        @returns: amount of height changes made to nodes
        """
    
    def insert_to_empty_tree(self, key, val):
        self.root = AVLNode(key, val)
        self.root.make_leaf()
        self.max = self.root
        return 0

    """"Insert the new node like a regular BS tree

        @rtype: AVLNode
        @returns: the parent of the newly inserted node
        """
    
    def regular_insert(self, key, val):
        temp_node = self.root
        temp_node_parent = temp_node.get_parent()

        new_node = AVLNode(key, val)

        while (temp_node.get_height() != -1):
            if (temp_node.get_key() < key):
                temp_node_parent = temp_node
                temp_node = temp_node.get_right()
            else:
                temp_node_parent = temp_node
                temp_node = temp_node.get_left()

        if (temp_node_parent.get_key() < key):
            temp_node_parent.set_right(new_node)
            temp_node_parent.get_right().set_parent(temp_node_parent)
            temp_node_parent.get_right().make_leaf()
        else:
            temp_node_parent.set_left(new_node)
            temp_node_parent.get_left().set_parent(temp_node_parent)
            temp_node_parent.get_left().make_leaf()

        return temp_node_parent

    """Rotate the sub tree of "AVL offender"

        @type node: AVLNode
        @param node: the "AVL offender" node
        @type bf: int
        @pre bf: bf == -2 or bf == 2
        @param bf: the balance factor of the "AVL offender" node
        @rtype: int
        @returns: number of rotations made
        """
    
    def rotate(self, node, bf):
        direction = node.get_direction()

        if (bf == -2):
            right_bf = node.get_right().get_balance_factor()
            if (right_bf == -1 or right_bf == 0):
                return self.left_rotation(node, direction)
            elif (right_bf == 1):
                return self.right_left_rotation(node, direction)

        elif (bf == 2):
            left_bf = node.get_left().get_balance_factor()
            if (left_bf == -1):
                return self.left_right_rotation(node, direction)
            elif (left_bf == 1 or left_bf == 0):
                return self.right_rotation(node, direction)

    """Left rotation

        @type node: AVLNode
        @param node: the "AVL offender" node
        @type direction: string
        @param direction: the direction of the node according to its parent
        @rtype: int
        @returns: number of rotations made
        """
    
    def left_rotation(self, node, direction):
        child = node.get_right()
        node.set_right(child.get_left())
        node.get_right().set_parent(node)
        child.set_left(node)
        child.set_parent(node.get_parent())

        if (direction == "right"):
            child.get_parent().set_right(child)
        elif (direction == "left"):
            child.get_parent().set_left(child)
        elif (direction == "root"):
            self.root = child

        node.set_parent(child)

        """" Update the height and size of the affected nodes """
        node.update_height_and_size()
        child.update_height_and_size()

        return 1

    """Left right rotation

        @type node: AVLNode
        @param node: the "AVL offender" node
        @type direction: string
        @param direction: the direction of the node according to its parent
        @rtype: int
        @returns: number of rotations made
        """
    
    def left_right_rotation(self, node, direction):
        child = node.get_left()
        grand_child = child.get_right()

        child.set_right(grand_child.get_left())
        child.get_right().set_parent(child)
        node.set_left(grand_child.get_right())
        node.get_left().set_parent(node)

        grand_child.set_left(child)
        grand_child.set_right(node)

        grand_child.set_parent(node.get_parent())
        node.set_parent(grand_child)
        child.set_parent(grand_child)

        if (direction == "right"):
            grand_child.get_parent().set_right(grand_child)
        elif (direction == "left"):
            grand_child.get_parent().set_left(grand_child)
        elif (direction == "root"):
            self.root = grand_child

        """" Update the height and size of the affected nodes """
        node.update_height_and_size()
        child.update_height_and_size()
        grand_child.update_height_and_size()

        return 2

    """Right rotation

        @type node: AVLNode
        @param node: the "AVL offender" node
        @type direction: string
        @param direction: the direction of the node according to its parent
        @rtype: int
        @returns: number of rotations made
        """
    
    def right_rotation(self, node, direction):
        child = node.get_left()
        node.set_left(child.get_right())
        node.get_left().set_parent(node)

        child.set_right(node)
        child.set_parent(node.get_parent())

        if (direction == "right"):
            child.get_parent().set_right(child)
        elif (direction == "left"):
            child.get_parent().set_left(child)
        elif (direction == "root"):
            self.root = child

        node.set_parent(child)

        """" Update the height and size of the affected nodes """
        node.update_height_and_size()
        child.update_height_and_size()

        return 1

    """Right left rotation

        @type node: AVLNode
        @param node: the "AVL offender" node
        @type direction: string
        @param direction: the direction of the node according to its parent
        @rtype: int
        @returns: number of rotations made
        """
    
    def right_left_rotation(self, node, direction):
        child = node.get_right()
        grand_child = child.get_left()

        child.set_left(grand_child.get_right())
        child.get_left().set_parent(child)
        node.set_right(grand_child.get_left())
        node.get_right().set_parent(node)

        grand_child.set_left(node)
        grand_child.set_right(child)

        grand_child.set_parent(node.get_parent())
        node.set_parent(grand_child)
        child.set_parent(grand_child)

        if (direction == "right"):
            grand_child.get_parent().set_right(grand_child)
        elif (direction == "left"):
            grand_child.get_parent().set_left(grand_child)
        elif (direction == "root"):
            self.root = grand_child

        """" Update the height and size of the affected nodes """
        node.update_height_and_size()
        child.update_height_and_size()
        grand_child.update_height_and_size()

        return 2

    """deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def delete(self, node):

        BF_cnt = 0

        temp_tuple = self.regular_delete(node)
        parent = temp_tuple[0]
        BF_cnt += temp_tuple[1]

        while (parent != None):
            prev_height = parent.get_height()
            parent.update_height_and_size()
            bf = parent.get_balance_factor()
            if (abs(bf) < 2 and parent.get_height() == prev_height):
                break
            elif (abs(bf) < 2 and parent.get_height() != prev_height):
                BF_cnt += 1
                parent = parent.get_parent()
            elif (abs(bf) == 2):
                BF_cnt += self.rotate(parent, bf)
                parent = parent.get_parent()

        """" Continue to go up to the root to update the height and size of nodes """
        BF_cnt += self.continue_to_update(parent)

        return BF_cnt

    """Delete the given node as if the tree is a regular binary tree

        @type node: AVLNode
        @pre node: node is a real pointer to a node in self
        @param node: the node to be deleted
        @rtype: (AVLNode, int)
        @returns: a tuple of the parent of the deleted node and the amount of height changes made to nodes
        """
    
    def regular_delete(self, node):
        direction = node.get_direction()
        BF_cnt_temp = 0
        parent = node.get_parent()

        if (node.is_leaf()):
            if (direction == "left"):
                node.get_parent().set_left(virtualNode)
            elif (direction == "right"):
                node.get_parent().set_right(virtualNode)
            else:
                self.root = None
        elif (node.is_only_one_child_left()):
            if (direction == "left"):
                node.get_parent().set_left(node.get_left())
                node.get_left().set_parent(node.get_parent())
            elif (direction == "right"):
                node.get_parent().set_right(node.get_left())
                node.get_left().set_parent(node.get_parent())
            else:
                self.root = node.get_left()
                self.root.set_parent(None)
        elif (node.is_only_one_child_right()):
            if (direction == "left"):
                node.get_parent().set_left(node.get_right())
                node.get_right().set_parent(node.get_parent())
            elif (direction == "right"):
                node.get_parent().set_right(node.get_right())
                node.get_right().set_parent(node.get_parent())
            else:
                self.root = node.get_right()
                self.root.set_parent(None)
        else:
            successor_node = node.successor()
            temp_tuple = self.regular_delete(successor_node)
            parent = temp_tuple[0]
            BF_cnt_temp += temp_tuple[1]

            if (parent == node):
                parent = successor_node
            
            successor_node.set_parent(node.get_parent())
            if (direction == "left"):
                successor_node.get_parent().set_left(successor_node)
            elif (direction == "right"):
                successor_node.get_parent().set_right(successor_node)
            else:
                self.root = successor_node
            successor_node.set_left(node.get_left())
            successor_node.get_left().set_parent(successor_node)
            successor_node.set_right(node.get_right())
            successor_node.get_right().set_parent(successor_node)
            prev_height = successor_node.get_height()
            successor_node.update_height_and_size()
            if (prev_height != successor_node.get_height()):
                BF_cnt_temp += 1

        return (parent, BF_cnt_temp)


    """returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""

    def avl_to_array(self):
        if (self.root == None):
            return []
        lst = []
        self.avl_to_array_rec(self.root, lst)
        return lst

    """Recurstion version of avl_to_array

        @type node: AVLNode
        @param node: the root of the current sub tree
        @type lst: list
        @param lst: the list of added nodes so far
        @rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
        """
    
    def avl_to_array_rec(self, node, lst):
        if (node != virtualNode):
            self.avl_to_array_rec(node.get_left(), lst)
            lst += [(node.get_key(), node.get_value())]
            self.avl_to_array_rec(node.get_right(), lst)

    """returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""

    def size(self):
        if (self.root == None):
            return 0
        return self.get_root().get_size()

    """splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: The intended node in the dictionary according to whom we split
	@rtype: list
	@returns: a list [left, right], where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""

    def split(self, node):
        left_tree = AVLTree()
        left_tree.root = node.get_left()

        if (left_tree.root == virtualNode):
            left_tree.root = None

        right_tree = AVLTree()
        right_tree.root = node.get_right()

        if (right_tree.root == virtualNode):
            right_tree.root = None

        node.disconnect()

        lst = [left_tree, right_tree]
        
        while (node.get_parent() != None):
            parent = node.get_parent()
            temp_tree = AVLTree()
            if (parent.get_right() == node):
                temp_tree.root = parent.get_left()
                parent.disconnect()
                left_tree.join(temp_tree, parent.get_key(), parent.get_value())
            else:
                temp_tree.root = parent.get_right()
                parent.disconnect()
                right_tree.join(temp_tree, parent.get_key(), parent.get_value())
            node = parent

        if left_tree.get_root() != None:
            left_tree.get_root().set_parent(None)
        if right_tree.get_root() != None:
            right_tree.get_root().set_parent(None)

        self.root = None

        return lst


    """joins self with key and another AVLTree

	@type tree: AVLTree 
	@param tree: a dictionary to be joined with self
	@type key: int 
	@param key: The key separting self with tree
	@type val: any 
	@param val: The value attached to key
	@pre: all keys in self are smaller than key and all keys in tree are larger than key,
	or the other way around.
	@rtype: int
	@returns: the absolute value of the difference between the height of the AVL trees joined
	"""

    def join(self, tree, key, val):

        new_node = AVLNode(key, val)
        new_node.make_leaf()

        """ Checks if one of the trees is empty """
        if (self.get_root() == None and tree.get_root() == None):
            self.root = new_node
            return 1
        elif (self.get_root() == None):
            tree.insert(key, val)
            height_difference = tree.get_root().get_height() + 2
            self.root = tree.get_root()
            tree.root = None
            return height_difference
        elif (tree.get_root() == None):
            self.insert(key, val)
            height_difference = self.get_root().get_height() + 2
            return height_difference


        """ Check which tree has smaller keys than the new key """
        if (self.root.get_key() > key):
            temp_node = self.root
            self.root = tree.get_root()
            tree.root = temp_node

        if (self.root.get_height() <= tree.get_root().get_height()):
            lower_tree = self.root
            heigher_tree = tree.get_root()
            height_difference = self.join_right_heigher(heigher_tree, lower_tree, new_node)
        else:
            lower_tree = tree.get_root()
            heigher_tree = self.root
            height_difference = self.join_left_heigher(heigher_tree, lower_tree, new_node)

        return height_difference
    
    """Join the trees with the left tree (with the smaller keys) being heigher

        @type heigher_tree: AVLNode
        @param heigher_tree: the root of the heigher tree
        @type lower_tree: AVLNode
        @param lower_tree: the root of the lower tree
        @type new_node: AVLNode
        @param new_node: the new node to make the conjunction at
        @rtype: int
        @returns: the height difference of both trees before the conjuction 
        """
    
    def join_left_heigher(self, heigher_tree, lower_tree, new_node):
        """" Calculate the height difference """
        height_difference = heigher_tree.get_height() - lower_tree.get_height() + 1

        heigher_tree_subtree = self.travel_right(heigher_tree, lower_tree.get_height())
        heigher_tree = heigher_tree_subtree.get_parent()

        """" Create new subtree with the new node as the root """
        new_node.set_right(lower_tree)
        lower_tree.set_parent(new_node)
        new_node.set_left(heigher_tree_subtree)
        heigher_tree_subtree.set_parent(new_node)
        new_node.update_height_and_size()

        """" Attach the new root to left overs of heigher tree and rebalance as necessary """
        new_node.set_parent(heigher_tree)
        self.root = new_node
        if (heigher_tree != None):
            self.root = heigher_tree
            heigher_tree.set_right(new_node)
            self.fix_left_overs(heigher_tree)

        return height_difference

    """Travel right on heigher tree until you reach height of h or h-1 of lower tree

        @type node: AVLNode
        @param node: the root of the heigher tree
        @type height: int
        @param node: the height to stop at
        @rtpye: AVLNode
        @returns: the node in the higher tree to connect as the right child of the new node
        """
    
    def travel_right(self, node, height):
        temp_node = node
        while (temp_node.get_height() > height):
            temp_node = temp_node.get_right()
        return temp_node

    """Join the trees with the right tree (with the bigger keys) being heigher

        @type heigher_tree: AVLNode
        @param heigher_tree: the root of the heigher tree
        @type lower_tree: AVLNode
        @param lower_tree: the root of the lower tree
        @type new_node: AVLNode
        @param new_node: the new node to make the conjunction at
        @rtype: int
        @returns: the height difference of both trees before the conjuction 
        """
    
    def join_right_heigher(self, heigher_tree, lower_tree, new_node):
        """" Calculate the height difference """
        height_difference = heigher_tree.get_height() - lower_tree.get_height() + 1

        heigher_tree_subtree = self.travel_left(heigher_tree, lower_tree.get_height())
        heigher_tree = heigher_tree_subtree.get_parent()

        """" Create new subtree with the new node as the root """
        new_node.set_left(lower_tree)
        lower_tree.set_parent(new_node)
        new_node.set_right(heigher_tree_subtree)
        heigher_tree_subtree.set_parent(new_node)
        new_node.update_height_and_size()

        """" Attach the new root to left overs of heigher tree and rebalance as necessary """
        new_node.set_parent(heigher_tree)
        self.root = new_node
        if (heigher_tree != None):
            self.root = heigher_tree
            heigher_tree.set_left(new_node)
            self.fix_left_overs(heigher_tree)

        return height_difference

    """"Travel left on heigher tree until you reach height of h or h-1 of lower tree

        @type node: AVLNode
        @param node: the root of the heigher tree
        @type height: int
        @param node: the height to stop at
        @rtpye: AVLNode
        @returns: the node in the higher tree to connect as the left child of the new node
        """
    
    def travel_left(self, node, height):
        temp_node = node
        while (temp_node.get_height() > height):
            temp_node = temp_node.get_left()
        return temp_node

    """Continue to go up the tree to the new root, fixing height and sizes
        and rotating as needed

        @type heigher_tree: AVLNode
        @param heigher_tree: the parent of the conjunction node
        @returns: None
        """
    
    def fix_left_overs(self, heigher_tree):
        while (heigher_tree.get_parent() != None):
            heigher_tree.update_height_and_size()
            bf = heigher_tree.get_balance_factor()
            if (abs(bf) < 2):
                heigher_tree = heigher_tree.get_parent()
                self.root = heigher_tree
            else:
                """temporarily disconnect higher_tree from his parent in order to rotate properly"""
                heigher_tree_old_parent = heigher_tree.get_parent()

                direction = heigher_tree.get_direction()
                if direction == "left":
                    heigher_tree.get_parent().set_left(virtualNode)
                else:
                    heigher_tree.get_parent().set_right(virtualNode)
                heigher_tree.set_parent(None)

                self.rotate(heigher_tree, bf)

                """reconnection the parent to his new son"""
                if direction == "left":
                    heigher_tree_old_parent.set_left(self.root)
                else:
                    heigher_tree_old_parent.set_right(self.root)
                self.root.set_parent(heigher_tree_old_parent)
                
                heigher_tree = heigher_tree_old_parent
                self.root = heigher_tree

        heigher_tree.update_height_and_size()
        bf = heigher_tree.get_balance_factor()
        if (abs(bf) == 2):
            self.rotate(heigher_tree, bf)

    """compute the rank of node in the self

	@type node: AVLNode
	@pre: node is in self
	@param node: a node in the dictionary which we want to compute its rank
	@rtype: int
	@returns: the rank of node in self
	"""

    def rank(self, node):
        current_rank = node.get_left().get_size() + 1
        temp_node = node

        while (temp_node.get_parent() != None):   
            if (temp_node == temp_node.get_parent().get_right()):
                current_rank += temp_node.get_parent().get_left().get_size() + 1
            temp_node = temp_node.get_parent()

        return current_rank

    """finds the i'th smallest item (according to keys) in self

	@type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@rtype: int
	@returns: the item of rank i in self
	"""

    def select(self, i):
        return self.select_rec(i, self.root)

    """Recurstion version of select)

        @type i: int
	@pre: 1 <= i <= self.size()
	@param i: the rank to be selected in self
	@type node: AVLNode
	@pre: the root of the current sub tree to search in
	@param node: the node to start search for the selected node at
	@rtype: int
	@returns: the item of rank i in self
        """
    
    def select_rec(self, i, node):
        current_rank = node.get_left().get_size() + 1

        if (i == current_rank):
            return node
        elif (i < current_rank):
            return self.select_rec(i, node.get_left())
        else:
            return self.select_rec(i - current_rank, node.get_right())


    """returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""

    def get_root(self):
        return self.root
