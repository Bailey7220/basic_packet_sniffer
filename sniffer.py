from scapy.all import *   # .all for Scapy core functions # import * to import everything defined in scapy.all, rather than one at a time.

def packet_callback(packet):
    if packet.haslayer(TCP):        
        print (f"TCP Packet: {packet[IP].src} -> {packet[IP].dst}")

sniff(prn=packet_callback, store=0, filter="tcp") #sniff function captures packets. # count= defines the amount of packets to be captured. # prn= sends packet to stated function
