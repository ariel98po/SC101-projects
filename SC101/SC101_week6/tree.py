"""
File: tree.py
Name: 
-------------------------
This file shows the basic concepts for binary trees.
After constructing a tree, we will do 3 traversal examples:
Pre-order
In-order 
Post-order
"""

class Tree:
	def __init__(self, left, tree_value, right):
		self.left = left
		self.tree_value = tree_value
		self.right = right


def main():
	leaf1 = Tree(None, 2, None)
	leaf2 = Tree(None, 6, None)
	leaf3 = Tree(None, 18, None)
	leaf4 = Tree(None, 40, None)
	node1 = Tree(leaf1, 4, leaf2)
	node2 = Tree(leaf3, 19, leaf4)
	root = Tree(node1, 17, node2)
	pre_order(root)
	in_order(root)
	post_order(root)

def traversal(root):

	if root is None:
		pass

	else:
		print(root.tree_value)
		traversal(root.left)
		traversal(root.right)


def pre_order(root):

	if root is None:
		pass

	else:
		print(root.tree_value)
		pre_order(root.left)
		pre_order(root.right)


def in_order(root):
	if root is None:
		pass

	else:

		in_order(root.left)
		print(root.tree_value)
		in_order(root.right)


def post_order(root):
	if root is None:
		pass
	else:

		post_order(root.left)
		post_order(root.right)
		print(root.tree_value)

	

if __name__ == '__main__':
	main()
