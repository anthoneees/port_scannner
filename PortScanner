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
    socket.setdefaulttimeout(1)
    try:
        result = s.connect_ex((target, port))
        if result == 0:
            serviceName = socket.getservbyport(port, "tcp")
            print("Port :", port, "is open. ")
            print("Service running at port %d is %s"%(port, serviceName))
        else:
            pass
        result.close()
    except socket.error:
        print("socket.error exception")
        sys.exit()
    except socket.gaierror:
        print("socket.gaierror exception")
        sys.exit()
count=1
for x in range(1,5000):
    t=threading.Thread(target=port_scanner,kwargs={'port':count})
    count+=1
    t.start()
print("done scanning")
