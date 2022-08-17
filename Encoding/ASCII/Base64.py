import base64
str = b'Hello World'
print(base64.b64encode(str))


import base64
str2 = b'SGVsbG8gV29ybGQ='
print(base64.b64decode(str2))
