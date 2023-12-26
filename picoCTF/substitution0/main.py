import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase

upper_key = "ZGSOCXPQUYHMILERVTBWNAFJDK"
lower_key = upper_key.lower()

flag = []
 
with open("message.txt") as file :
	content = file.read()

for char in content : 
	if char.isupper() :
		position = upper_key.index(char)
		flag.append(upper[position])
	elif char.islower() :
		position = lower_key.index(char)
		flag.append(lower[position])
	else : 
		flag.append(char)
		
flag = "".join(flag)
print(flag.split()[-1])
	
