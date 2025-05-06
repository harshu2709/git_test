from scapy.all import sniff
import time 

def packet_callback(packet):
	print(packet.show())
	
for i in range(5):
	sniff(prn=packet_callback, store=0, count=1)
	time.sleep(1)
	
