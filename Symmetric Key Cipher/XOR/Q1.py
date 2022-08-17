enc_str = "41564b39706a396a76397c786a60383838"

enc_str = bytes.fromhex(enc_str)
	p = ''
	for c in enc_str:
		p = p + chr(c^i)
	print(i,p)
