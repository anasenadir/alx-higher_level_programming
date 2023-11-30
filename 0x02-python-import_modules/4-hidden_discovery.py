#!/usr/bin/python3
if __name__ == "__main__":
	import hidden_4
	for fun_name in dir(hidden_4):
		if fun_name[0] != '_':
			print(fun_name)
