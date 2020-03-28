# sending binary files to another VM without passing the ping 100 limit
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import threading
from scapy.all import *

ping = Ether()/IP(dst="10.0.2.4")/ICMP()/Raw()

f = open("nc", "rb")
size = (100 - len(ping)) # ping packet can be of a maximum of 100

def loop1_10():
	for i in range (30):
		ping['Raw'].load = f.read(size)
		srp1(ping, timeout = 1)

# read and send to Ubuntu VM
while f:
	threading.Thread(target = loop1_10).start()
#	ping['Raw'].load = f.read(size)
#	srp1(ping, timeout = 1)
f.close()

#Finish end exit sniff on the Ubuntu VM
ping['Raw'].load = 'Finished'
srp1(ping, timeout = 1)

