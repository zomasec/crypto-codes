## XOR properties :

> 
> 
> 1. **Commutative Property**: The order of operands does not affect the result of XOR. In other words, A XOR B is equal to B XOR A.
>     - Example: A XOR B = B XOR A
> 2. **Associative Property**: The grouping of operands does not affect the result of XOR. That is, (A XOR B) XOR C is equal to A XOR (B XOR C).
>     - Example: (A XOR B) XOR C = A XOR (B XOR C)
> 3. **Identity Property**: There is no identity element for XOR in the same way that 0 is the identity element for addition and 1 is for multiplication.
> 4. **Inverse Property**: XORing a value with itself results in 0. In other words, A XOR A equals 0 for any value of A.
>     - Example: A XOR A = 0
> 5. **Self-Inverse Property**: XORing a value with another value twice results in the original value. In other words, A XOR B XOR B equals A.
>     - Example: A XOR B XOR B = A

Challenge :
Let's put this into practice! Below is a series of outputs where three random keys have been XORed together and with the flag. Use the above properties to undo the encryption in the final line to obtain the flag.

```python
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
```

Challenge solve :
