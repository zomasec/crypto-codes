import string

alphs = string.ascii_uppercase
digs = string.digits

flag = []
with open("message.txt") as file :
	content = file.read()
	numbers = [int(val) for val in content.split()]
	for num in numbers :
		mod = pow(num, -1, 41)
		if mod in range(1, 27) :
			flag.append(alphs[mod - 1])
		elif mod in range(27, 37) :
			flag.append(digs[mod - 27])
		else :
			flag.append('_')
	file.close()
	
print("picoCTF{%s}" % "".join(flag))
