# 1-Intro

What is ASCII ??

ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.

`char()` function used to convert any char to the representation of it in ASCII . 

`ord()` function used to do the reverse of `char()` , used to covert any ASCII number to character.

The challenge :

Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.

```python
[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
```

The challenge solve :

```python
ords = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

chars = ''.join(chr(o) for o in ords )

print(chars)
```
