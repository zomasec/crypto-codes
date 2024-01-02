# 2-HEX

When we encrypt data the cyphertext commonly has bytes which are not printable characters , so we should encode it to something else.

ASCII characters are represented by numbers ranging from `0 to 127` (or `0x00 to 0x7F` in hexadecimal), and they include letters, digits, punctuation marks, and control characters. However, when data is encrypted, it might involve operations that produce byte values outside this ASCII range.

Hexadecimal can be used in such a way to represent ASCII strings

Each hexadecimal digit represents four bits so the two digits in hex represents 8 nits which is one byte 

The challenge :

Included below is a flag encoded as a hex string. Decode this back into bytes to get the flag.

```python
63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d
```

> In Python, the `bytes.fromhex()` function can be used to convert hex to bytes. The `.hex()` instance method can be called on byte strings to get the hex representation.
> 

The challenge solve :

```python
hex_string = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'

# Convert hex string to bytes
decoded_bytes = bytes.fromhex(hex_string)

# Print the decoded bytes
print(decoded_bytes.decode('utf-8'))
```

or you can use :

```python
from binascii import unhexlify

hex_string = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'

# Convert hex string to bytes
decoded_bytes = unhexlify(hex_string)

# Print the decoded bytes
print(decoded_bytes)
```

- Note :
    
    In Python, when you have a sequence of bytes (a **`bytes`** object), you can decode it into a string using a specific character encoding. The **`decode()`** method is used to convert these bytes into a human-readable string by specifying the encoding.
    
    When you decode the bytes using **`decode('utf-8')`**, you're telling Python to interpret these bytes as UTF-8 encoded text. UTF-8 is a widely used encoding that can represent most characters in the Unicode standard. If the bytes were originally text encoded in UTF-8, decoding them with this method will correctly convert them back to their original string form.
    
    If you don't explicitly decode the bytes, and you simply print the bytes object, Python will try to display the raw bytes as a representation. This might not be human-readable, especially if the bytes contain non-printable characters or characters that don't have a direct visual representation.
    
    Let's consider an example:
    
    ```python
    pythonCopy code
    decoded_bytes = bytes.fromhex("48656C6C6F21")  # Hexadecimal representation of "Hello!"
    
    # Print the bytes without decoding
    print(decoded_bytes)
    
    ```
    
    The output without decoding the bytes would be something like: **`b'Hello!'`**. This indicates that the data is stored as bytes but displayed in a way that indicates it's textual data.
    
    By decoding the bytes using **`decode('utf-8')`**, you get the string representation directly: **`"Hello!"`**.
    
    If the bytes were originally encoded in a different encoding (e.g., UTF-16, Latin-1, etc.), decoding them with the wrong encoding would result in garbled text or errors because the interpretation of bytes as characters depends on the correct encoding being used.
    

[ASCII table](https://www.rapidtables.com/code/text/ascii-table.html)

[Wikipedia: Hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal)

###
