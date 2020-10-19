"""
File: adv_permutation.py
Name:
------------------------------
This program finds all the permutations [1, 2, 3].
To complete this task, you will need backtracking
-- choose, explore, and un-choose
"""


def main():
	permutation([1, 2, 3])


def permutation(lst):
	pemutation_helper(lst, [], len(lst))

def pemutation_helper(lst, current_list, target_length):

	if len(current_list) == target_length:
		print(current_list)

	else:
		for num in lst:

			if num not in current_list:

				# Choose
				current_list.append(num)

				# Explore
				pemutation_helper(lst, current_list, target_length)

				# Un-choose
				current_list.pop()






if __name__ == '__main__':
	main()