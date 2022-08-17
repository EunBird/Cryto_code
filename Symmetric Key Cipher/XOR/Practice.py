def EnCrypt(inputString):
	xorKey = 'P'
	
	ret = ''
	for ch in inputString:
		ret = ret + chr(ch ^ ord(xorKey))
		
	return ret
	
text = b "Hello XOR"

ciphertext = EnDecrypt(text)
print("CipherText :", bytes(ciphertext, 'utf-8').hex())

plaintext = EnDecrypt(ciphertext.encode())
print("PlainText :", plaintext)
