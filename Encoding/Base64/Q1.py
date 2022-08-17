import base64

hex_str = "4261736531362c204261736533322c20616e642042617365363420616c676f726974686d73"

byte = bytes.fromhex(hex_str)

print(byte)

str = base64.b64encode(byte)
print(str)

# FLAG : b'Base16, Base32, and Base64 algorithms'
