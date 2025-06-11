from scapy.all import sniff, IP, conf
import pandas as pd
import os

features = []

def packet_callback(packet):
    if packet.haslayer(IP):
        proto = packet[IP].proto
        src = packet[IP].src
        dst = packet[IP].dst
        length = len(packet)
        features.append([src, dst, proto, length])

# ✅ Make sure "data" folder exists
if not os.path.exists("data"):
    os.makedirs("data")

print("🔍 Capturing 100 packets... do some internet activity now!")
sniff(count=100, prn=packet_callback, iface=conf.iface, filter="ip", store=False)

df = pd.DataFrame(features, columns=["SourceIP", "DestIP", "Protocol", "Length"])
df["Label"] = "normal"  # Default label
df.to_csv("data/traffic.csv", index=False)

print(" Packet data saved to data/traffic.csv")
print(df.head())
