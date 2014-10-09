#encoding:utf-8
import socket
import sys
from thread import *

HOST = 'localhost'   #choose at ease
PORT = 8885          #choose at ease

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print 'Socket created'

#Bind socket to localhost and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

#Start listening on socket
s.listen(10)#10 means largest amount of connections
print 'Socket now listening'

#Function for handling connections. This will be used to create threads
def connectionHandlingThread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string

    #infinite loop so that function do not terminate and thread do not end.
    while True:

        #Receiving from client
        data = conn.recv(1024)#1024 means the size of buffer
        reply = 'OK...' + data
        if not data:
            break

        conn.sendall(reply)

    #came out of loop
    conn.close()

#now keep talking with the client
while True:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(connectionHandlingThread ,(conn,))

s.close()
