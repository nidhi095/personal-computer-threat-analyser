# personal-computer-threat-analyser

A real-time network traffic sniffer and basic intrusion detection system built using Python, Scapy, and machine learning (Random Forest). It classifies network packets as **normal** or various types of **attacks** like `udp_flood`, `syn_flood`, `http_flood`, etc.

---

## 📁 Project Structure

```

cybersecurity-packet-detector/
│
├── sniff\_packets.py          # Captures packets and saves to CSV
├── extract\_features.py       # Extracts IP, protocol, length from packets
├── train\_model.py            # Trains Random Forest on the packet data
├── real\_time\_detect.py       # Real-time attack detection and classification
│
├── model.pkl                 # Trained Random Forest model
├── label\_mapping.csv         # Maps label numbers to attack names
├── requirements.txt          # Dependencies
├── README.md                 # Project overview
│
└── data/
└── traffic.csv           # Collected packet data (with labels)

````

---

## 🚀 How to Run

> ⚠️ This project requires **Npcap** to be installed on Windows for Scapy to sniff packets.  
> Download from: [https://nmap.org/npcap](https://nmap.org/npcap)

### 🔹 1. Install Dependencies

```bash
pip install -r requirements.txt
````

### 🔹 2. Capture Packets

This script captures 100 packets and stores their features in `data/traffic.csv`.

```bash
python sniff_packets.py
```

> Tip: Do some internet activity during capture (e.g., open websites, ping, etc.)

### 🔹 3. Label Attacks in CSV

Open `data/traffic.csv` and manually label a few rows with attacks like:

* `udp_flood`
* `syn_flood`
* `ping_flood`
* `tcp_scan`
* `http_flood`
* `dns_amplification`
* `smurf_attack`

Save and close the CSV.

### 🔹 4. Train the Detection Model

```bash
python train_model.py
```

This will generate `model.pkl` and `label_mapping.csv`.

### 🔹 5. Run Real-Time Detection

```bash
python real_time_detect.py
```

Watch as it classifies live packets and shows:

```
Detected: UDP_FLOOD | Protocol: 17 | Length: 1500
Detected: NORMAL     | Protocol: 6  | Length: 60
```

---

## 📦 Requirements

```
scapy
pandas
scikit-learn
joblib
```

---

## ✅ Features

* [x] Real-time packet sniffing
* [x] Feature extraction (IP, Protocol, Length)
* [x] Custom labeling and attack detection
* [x] ML-based classification (Random Forest)
* [x] Easily extendable to detect more attack types

---

## 🧠 Future Ideas

* Use SHAP or feature importance visualization
* Add anomaly detection (unsupervised)
* Build a Tkinter or web-based dashboard
* Log attacks to a file or alert user

---

## ⚠️ Disclaimer

This project is for **educational and research purposes only**. It does not actively prevent or block threats — only detects and labels traffic patterns using a trained model. Use responsibly.

---

