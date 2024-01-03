# 3-base64

### **Encoding Process:**

- **Conversion to 6-bit Groups:** Base64 takes groups of three bytes (24 bits total) from the original binary data.
- **Breaking into 6-bit Blocks:** These 24 bits are then divided into four 6-bit blocks.
- **Mapping to Characters:** Each 6-bit block is represented as a character in the Base64 alphabet. Base64 uses a set of 64 characters (A-Z, a-z, 0-9, '+' and '/') to represent these 6-bit values.
- **Padding (if needed):** If the total length of the binary data is not a multiple of three bytes, padding is added to make it a multiple of 24 bits. This padding is represented by the '=' character.

### **Decoding Process:**

- **Reverse Operations:** To decode Base64 back into its original binary form, the process is reversed.
- **Conversion to 6-bit Blocks:** Each character in the Base64 string represents a 6-bit value.
- **Combining Blocks:** These 6-bit values are combined back into 24-bit groups (four 6-bit blocks).
- **Reassembling Bytes:** The resulting 24-bit groups are reassembled into their original byte format.

> In Python, after importing the base64 module with `import base64`, you can use the `base64.b64encode()` function to encode the data and `base64.b64decode()` .
> 

The challenge : 

> challenge
> 
> 
> Take the below hex string, *decode* it into bytes and then *encode* it into Base64.
> 
> ```python
> 72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf
> ```
> 

The solve code  :

```python
import base64
from binascii import unhexlify

# This is hex data
hexdata = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

# Convert hex to bytes 
bytesdata = unhexlify(hexdata)

# Convert bytes to base64
base64data = base64.b64encode(bytesdata)
print(base64data)
```

[WIKI](https://en.wikipedia.org/wiki/Base64)
