# UDP PINGER SERVER & CLIENT  #
# UDP PINGER SERVER & CLIENT  #
#     FURKANCAN B. YUCE       #
# UDP PINGER SERVER & CLIENT  #
# UDP PINGER SERVER & CLIENT  #

import socket
import sys
from timeit import default_timer as timer

BUFFER = 64
SENT_CYCLE = 10
TIMEOUT = 10
MESSAGE = "X" * BUFFER


def getLocalIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    IP = s.getsockname()[0]
    s.close()
    return IP

def server(UDP_PORT):

    UDP_PORT = int(UDP_PORT)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    sock.bind(("", UDP_PORT))
    sock.settimeout(TIMEOUT)

    print("[*] Server has started!")
    print("[*] Your local IPv4: ", getLocalIP() )
    print("[*] Waiting for data...\n")
    
    for x in range(SENT_CYCLE):
        data, addr = sock.recvfrom(BUFFER) 
        sock.sendto(data,addr)
        print("[*] Packet received and sent succesfully (: ")

def client(UDP_IP, UDP_PORT):

 
    UDP_PORT = int(UDP_PORT)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    
    RTT = []

    for i in range(SENT_CYCLE):
        #before = time.time()
        before = timer()
        sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
        data,addr = sock.recvfrom(BUFFER)
        #now = time.time()
        now = timer()
        diff = round((now - before)*1000 ,3)# Miliseconds
        RTT.append(diff)

        print("Reply from", UDP_IP, "in " , round(diff,3) , " mseconds") 

    SUMofRTT = sum(RTT)
    MAXofRTT = max(RTT)
    MINofRTT = min(RTT)

    print("\n[*] Round Trip Time --> Average: ", round(SUMofRTT/SENT_CYCLE,3) ,"ms" " Min: ", MINofRTT,"ms"," Max: ", MAXofRTT,"ms") 

def main():
   
    if sys.argv[1] == "-s":
        server(sys.argv[2]) 
    elif sys.argv[1]=="-c":
        client(sys.argv[2],sys.argv[3])


if __name__== "__main__":
    main()
