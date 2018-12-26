#!/usr/bin/python3

from random import randint
from sys import argv
from sys import exit

WORDFILE = "/usr/share/password-gen/words.csv"
helpText = """Usage: password-gen [--digits] [--help]
Example: password-gen --digits"""

"""
Generates a random password
"""
def password_gen(digits):
	words = [l.strip() for l in open(WORDFILE) if l[0] != "#"]
	passwd = [words[randint(0, len(words) - 1)].capitalize() for w in range(4)]
	if digits:
		passwd.append(str(randint(0, 10000)))
	return "".join(passwd)

if __name__ == "__main__":
	d = False
	if len(argv) == 2:
		if argv[1] == "--help":
			print(helpText)
			exit(0)
		elif argv[1] == "--digits":
			d = True
	print(password_gen(d))

