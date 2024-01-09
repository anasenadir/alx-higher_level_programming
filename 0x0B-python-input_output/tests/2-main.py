import sys

sys.path.append("../")
append_write = __import__("2-append_write").append_write

r = append_write("2-text.txt", "shdjhf sdjkfghsdjl sdfjkhgjsdfh sdfsjkghsdfjgh\n")

print(r)
