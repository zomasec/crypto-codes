# 6-XOR

XOR is a bitwise operator which returns 0 if the bits are the same, and 1 otherwise. In textbooks the XOR operator is denoted by ⊕, but in most challenges and programming languages you will see the caret `^` used instead.

![Screenshot 2024-01-01 072935.png](PHOTOS/XOR.png)

- For longer binary numbers we XOR bit by bit: `0110 ^ 1010 = 1100`.
- We can XOR integers by first converting the integer from decimal to binary.
- We can XOR strings by first converting each character to the integer representing the Unicode character.

Given the string `label`, XOR each character with the integer `13`. Convert these integers back to a string and submit the flag as `crypto{new_string}`.

Solve code :

```python
def StringXOR(text : str, key : int) -> str : 
    xored = ''.join(chr(ord(char) ^ key) for char in text)
    
    return xored

print("crypto{{{}}}".format(StringXOR("lable", 13)))
# or you can use xor() function from pwntools library 
```
