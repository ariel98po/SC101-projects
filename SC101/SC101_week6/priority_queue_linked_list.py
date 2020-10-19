"""
File: priority_queue.py
Name: 
--------------------------
This file shows how to construct a linked list 
from scratch and use it to implement a priority queue.
"""


# It controls the condition to break the input loop
EXIT = '-1'


class LinkedList:
	def __init__(self, value, next_one):
		self.value = value
		self.next = next_one


def main():
	linked_list = LinkedList(None, None)
	while True:
		name = input(f'Name of patient ({EXIT} to quit): ')
		if name == EXIT:
			break
		priority = int(input('Priority: '))
		if linked_list.value is None:
			linked_list.value = (name, priority)
		else:

			# Prepend
			if priority < linked_list.value[1]:
				# New node at the beginning
				node = LinkedList((name, priority), None)
				node.next = linked_list
				linked_list = node

			# In-Between and Append
			else:
				current = linked_list
				while current.next is not None:
					if current.value[1] <= priority < current.next.value[1]:
						# New node in between
						node = LinkedList((name, priority), None)
						node.next = current.next
						current.next = node

						break
					current = current.next

				if current.next is None:
					# New node at the end
					current.next = LinkedList((name, priority), None)


	traversal(linked_list)


def traversal(linked_list):

	current = linked_list
	while current is not None:
		print(current.value)
		current = current.next


if __name__ == '__main__':
	main()
