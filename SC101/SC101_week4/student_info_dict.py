"""
File: student_info_dict.py
------------------------------
This program puts data in a text file 
into a nested data structure where key
is the name of each student, and the value
is the dict that stores the student info
"""


# The file name of our target text file
FILE = 'students_info.txt'


def main():
	all_d = {}
	######################
	with open(FILE, 'r') as f: #‘r’ – Read mode which is used when the file is only being read
		# first_line = f.readline()
		# print(first_line)
		for line in f:
			student_info_list = line.split()
			name = student_info_list[0]
			age = student_info_list[1]
			email = student_info_list[2]
			food = student_info_list[3:]

			student_d = {}
			student_d['AGE'] = age
			student_d['EMAIL'] = email
			student_d['FOOD'] = food


			all_d[name] = student_d



			# student_d ={
			# 	'AGE': student_info_list[1],
			# 	'EMAIL':student_info_list[2],
			# 	'FOOD': student_info_list[3]
			# }
			# all_d[student_info_list[0]] = student_d







	######################
	print_out_d(all_d)

	print(all_d['Jerry']['FOOD'][2])


def print_out_d(d):
	"""
	: param d: (dict) key of type str is the name of student
	                  value of type dict is the info of the student
	---------------------------------------------------------------
	This method prints out a nested data structure on console
	"""
	for name, name_d in d.items():
		print(name)
		print(name_d)
		# print(hex(id(name_d)))
		print('-----------------------------')




if __name__ == '__main__':
	main()