import socket
import sys
import threading
inp = input("What is target?(IP or domain name) ") #Asks user for input
target = socket.gethostbyname(inp) #takes user input and gets host IP with the given name
print("_" * 60) #formatting so that terminal is a bit easier to read
print("Scanning " + target)
print("_" * 60)
def port_scanner(port): #function that will detect open ports and running services 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create an INET, Streaming socket to communicate with server
    s.settimeout(.5) # sets timeout for socket object
    try:
        result = s.connect((target, port)) # connect client socket to server given an ip and port number
        serviceName = socket.getservbyport(port, "tcp") #find service name
        print("Port :", port, "is open. ")#prints any open ports
        print("Service running at port %d is %s"%(port, serviceName))#prints open services at each port 
        result.close()#destroy the connection
    except: #if port is closed skip it 
        pass
count=1
for x in range(1,5000):#runs through ports 
    t=threading.Thread(target=port_scanner,kwargs={'port':count}) #threading to speed up process of port scanning, thread instance 
    count+=1
    t.start() #starts threading
print("done scanning") # so user knows when the scanning processes are done 
