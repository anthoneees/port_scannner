import socket
import sys
import threading
inp = input("What is target?(IP or domain name) ")
target = socket.gethostbyname(inp)
print("_" * 60)
print("Scanning " + target)
print("_" * 60)
def port_scanner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(.5)
    try:
        result = s.connect((target, port))
        serviceName = socket.getservbyport(port, "tcp")
        print("Port :", port, "is open. ")
        print("Service running at port %d is %s"%(port, serviceName))
        result.close()
    except:
        pass
count=1
for x in range(1,5000):
    t=threading.Thread(target=port_scanner,kwargs={'port':count})
    count+=1
    t.start()
print("done scanning")
