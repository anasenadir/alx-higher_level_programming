#!/usr/bin/python3
if __name__ == "__main__":
	from sys import argv
	ar_count = len(argv) - 1
	print("{} arguments{}".format(ar_count, '.' if ar_count == 0 else ':'))
	for ar_i in range(1, ar_count + 1):
		print("{}: {}".format(ar_i, argv[ar_i]))
