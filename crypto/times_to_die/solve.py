import pyshark
import random

def xor(bytes1, bytes2):    
    return bytes(a ^ b for a, b in zip(bytes1, bytes2))

def decrypt(ciphertext, seed):
    random.seed(seed)
    blocks = []
    for i in range(0,len(ciphertext),4):
        ct_block = xor(ciphertext[i:i+4],random.randbytes(4))
        blocks.append(ct_block)
    plaintext = b''.join(blocks)
    return plaintext

def extract_data(pcapng_file):
    cap = pyshark.FileCapture(pcapng_file, display_filter='tcp.port == 1337')

    for packet in cap:
        try:
            tcp_data = bytes.fromhex(packet.DATA.data)
            time = float(packet.sniff_timestamp)
        except AttributeError: continue

    return tcp_data, time

data, time = extract_data('traffic.pcapng')

known = b'BCCT'
bt = xor(known,data[:4])
i = 0
t = int(time*2**16)
while True: # Brute force seed based off of time
    random.seed(t-i)
    if random.randbytes(4) == bt:
        key = t-i
        break
    i += 1

print(decrypt(data,key))