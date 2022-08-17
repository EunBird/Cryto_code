import base64

b64_msg = b'AQIDBAQGBwgJCgsMDQ4P/w=='

b64_decode=base64.b64decode(b64_msg)
print(b64_decode.hex())

