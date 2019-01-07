import socket

UDP_IP1 = "192.168.1.64"
UDP_IP2 = "192.168.1.73"
UDP_IP3 = "192.168.1.74"
UDP_PORT = 45           # used port on external device

port = 52129

message = "Message to observe..."      # not the real command string

def SendData():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  
        s.bind(("", port))
        msg = message.encode('utf-8')
        s.sendto(msg, (UDP_IP1, UDP_PORT))
    except:
        print("Sending Error!!!\n")

    return s

def ReceiveData(sock):
    print("Receiving data: \n")

    while True:
        data, addr = sock.recvfrom(4096)      # buffer size is 4096 bytes
        print ("received message:", data)


if __name__ == "__main__":    
    s = SendData()
    ReceiveData(s)