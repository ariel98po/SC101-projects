"""
File: student_info_dict.py
------------------------------
This program puts data in a text file 
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info
"""


# The file name of our target text file
FILE = 'romeojuliet.txt'

# Contains the chars we would like to ignore while processing the words
PUNCTUATION = '.,;!?#&-\'_+=/\\"@$^%()[]{}~'


def main():
	word_d = {}
	with open(FILE, 'r') as f:
		for line in f:
			words = line.split()
			for word in words:
				word = string_manipulation(word)
				if word in word_d:
					word_d[word] += 1
				else:
					word_d[word] = 1

	print_out_d(word_d)


def string_manipulation(word):
	ans = ''
	word = word.lower()
	for ch in word:
		if ch not in PUNCTUATION:
			ans += ch
	return ans


def print_out_d(d):
	"""
	: param d: (dict) key of type str is a word
	                  value of type int is the word occurrence
	---------------------------------------------------------------
	This method prints out all the info in d
	"""

	for word, counts in sorted(d.items(), key=lambda element: element[1]):

		print(f'{word}:{counts}')


if __name__ == '__main__':
	main()
