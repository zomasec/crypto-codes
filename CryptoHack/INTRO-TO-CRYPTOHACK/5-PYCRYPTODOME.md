# 5-PYCRYPTODOME

In cryptographic systems like RSA, mathematical operations are performed on numbers. However, messages are typically composed of characters or bytes. To apply mathematical operations on these messages in a cryptographic context, they need to be converted into numerical formats.

One common approach to converting messages into numbers is to:

1. **Obtain the Ordinal Bytes:** Get the ordinal (or ASCII) values of each character in the message. This converts each character into its corresponding byte value.
2. **Convert to Hexadecimal:** Convert these byte values into their hexadecimal representations.
3. **Concatenate Hexadecimal Values:** Concatenate the hexadecimal representations of the bytes together to form a larger hexadecimal number, which can then be interpreted as a base-16 number.
4. **Represent in Base-10/Decimal:** Optionally, the resulting base-16 number can also be represented in base-10/decimal form for easier manipulation or computation.

This process allows messages to be converted into a numerical format suitable for mathematical operations in cryptographic algorithms.

For instance, let's consider the message "HELLO":

1. The ASCII bytes of the characters "HELLO" are **`[72, 69, 76, 76, 79]`**.
2. The corresponding hexadecimal bytes are **`[0x48, 0x45, 0x4C, 0x4C, 0x4F]`**.
3. Concatenating these bytes gives the base-16 number **`0x48454C4C4F`**.
4. Interpreted in base-10, this becomes **`310400273487`**.

The `PyCryptodome` library in Python provides methods like **`bytes_to_long()`** and **`long_to_bytes()`** within **`Crypto.Util.number`** to handle these conversions conveniently.

The challenge :

Convert the following integer back into a message:

```
11515195063862318899931685488813747395775516287289682636499965282714637259206269
```

The solve code :

```python
from Crypto.Util.number import *

# This is long data 
LongData = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# Convert it to bytes 
BytesData = long_to_bytes(LongData)
# Then decode the bytes to string using UTF-8 
StringData = BytesData.decode('utf-8')

print(StringData)
```
