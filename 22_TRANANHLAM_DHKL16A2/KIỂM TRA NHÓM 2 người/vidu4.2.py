import pyshark

cap = pyshark.FileCapture('capture.pcapng')

print("=== Thông tin Tầng 2 (Data Link Layer - Ethernet) và Tầng 3 (Network Layer - IP) ===")
for packet in cap:
    try:
        # Tầng 2: Ethernet
        eth_src = packet.eth.src
        eth_dst = packet.eth.dst

        # Tầng 3: IP
        ip_src = packet.ip.src
        ip_dst = packet.ip.dst

        print(f"Ethernet: {eth_src} -> {eth_dst}")
        print(f"IP: {ip_src} -> {ip_dst}")
        print("-" * 50)

    except AttributeError:
        continue

cap.close()
