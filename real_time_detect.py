from scapy.all import sniff, IP, conf
import pandas as pd
import joblib

# Load model and label mapping
model = joblib.load("model.pkl")
label_map = pd.read_csv("label_mapping.csv")
label_dict = dict(zip(label_map["Label_Code"], label_map["Label"]))

def extract_features(packet):
    if packet.haslayer(IP):
        proto = packet[IP].proto
        length = len(packet)
        features = pd.DataFrame([[proto, length]], columns=["Protocol", "Length"])
        prediction = model.predict(features)[0]
        label = label_dict[prediction]
        print(f"Detected: {label.upper()} | Protocol: {proto} | Length: {length}")

# Run sniffing
print("Live detection started... Press Ctrl+C to stop.")
sniff(count=100, prn=extract_features, iface=conf.iface, filter="ip", store=False)
