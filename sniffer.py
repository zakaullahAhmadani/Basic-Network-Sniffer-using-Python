from scapy.all import sniff, IP, TCP, UDP

def process_packet(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]

        print("\n[+] Packet Captured")
        print("Source IP:", ip_layer.src)
        print("Destination IP:", ip_layer.dst)

        if packet.haslayer(TCP):
            print("Protocol: TCP")
        elif packet.haslayer(UDP):
            print("Protocol: UDP")
        else:
            print("Protocol: Other")

sniff(prn=process_packet, count=20)
