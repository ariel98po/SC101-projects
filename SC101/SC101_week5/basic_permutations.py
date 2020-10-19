"""
File: basic_permutations.py
Name:
-----------------------------
This program finds all the 3-digits binary permutations
by calling a recursive function binary_permutations.
Students will find a helper function useful in advanced
recursion problems.
"""


def main():
	binary_permutations(3)


def binary_permutations(n):
	binary_permutations_helper(n, '')


def binary_permutations_helper(n, current_str):
	if len(current_str) == n:
		print(current_str)
	else:
		binary_permutations_helper(n, current_str + '0')
		binary_permutations_helper(n, current_str + '1')

if __name__ == '__main__':
	main()