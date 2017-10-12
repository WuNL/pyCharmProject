from celery import Celery
import os
import sys
import time

from socket import *

HOST = "localhost"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)





app = Celery('tasks', backend='rpc://', broker='pyamqp://')
app.conf.result_backend = 'rpc://'

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

@app.task
def cliFun(data):
    if not data:
        print("no data")
    tcpCliSock.send(data.encode('utf8'))
    data=tcpCliSock.recv(BUFSIZ)
    if not data:
        print("recv no data")
    print(data.decode('utf8'))


@app.task
def cliFun1(data):
    if not data:
        print("no data")
    tcpCliSock.send(data.encode('utf8'))
    data=tcpCliSock.recv(BUFSIZ)
    if not data:
        print("recv no data")
    print("1"+data.decode('utf8'))

