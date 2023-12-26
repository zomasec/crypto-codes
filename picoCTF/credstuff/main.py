import string

def rot(text, rotation) :
	upper = string.ascii_uppercase
	lower = string.ascii_lowercase
	
	rotated_upper = upper[13:] + upper[:13] 
	rotated_lower = lower[13:] + lower[:13] 
	
	rot_table = str.maketrans(upper + lower, rotated_upper + rotated_lower)
	
	return text.translate(rot_table)

enc_flag = "cvpbPGS{P7e1S_54I35_71Z3}"

decr_flag = rot(enc_flag, 13)

print(decr_flag)
