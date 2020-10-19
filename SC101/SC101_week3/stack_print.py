
def main():
	stack = []
	while True:
		line = input('Give me a line:')
		if line == '-1':
			break
		stack.append(line)
	print_stack_out(stack)

def print_stack_out(s):
	while len(s) != 0:
		print(s.pop())



if __name__ == '__main__':
	main()