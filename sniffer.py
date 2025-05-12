from scapy.all import *   # .all for Scapy core functions # * to import everything defined in scapy.all, rather than one at a time.

def packet_callback(packet):
    print (packet.summary()) # packet.summary shows brief overview of packet

#Sniff a single packet and send it packet_callback
sniff(count=1, prn=packet_callback) #sniff function captures packets. # count= defines the amount of packets to be captured. # prn= sends packet to stated function
