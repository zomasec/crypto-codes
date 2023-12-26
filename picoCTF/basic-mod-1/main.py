#1/usr/bin/env python3


import string

alphs = string.ascii_uppercase
digs = string.digits
flag = []
with open("message.txt") as file :
	content = file.read()
	data = content.split()
	numbers = [ int(val) for val in data ]
	for num in numbers : 
		mod = num % 37
		if mod in range(26):
			flag.append(alphs[mod])
		elif mod in range(26, 36):
			flag.append(digs[mod - 26])
		else :
			flag.append('_')
			
	file.close()

print("picoCTF{%s}" % "".join(flag))
