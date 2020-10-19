"""
File: linked_list.py
Name: 
--------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""

class LinkedList:
	def __init__(self, value, next_one):
		self.value = value
		self.next = next_one


def main():
	data1 = LinkedList(8, None)
	linked_list = data1
	data2 = LinkedList(6, data1)
	linked_list = data2
	data3 = LinkedList(2, None)
	data3.next = data2
	linked_list = data3

	data4 = LinkedList(10, data3)
	linked_list = data4
	data5 = LinkedList(4, None)
	data5.next = data2
	data3.next = data5

	traversal(linked_list)

def traversal(linked_list):

	current = linked_list
	while current is not None:
		print(current.value)
		current = current.next






if __name__ == '__main__':
	main()
