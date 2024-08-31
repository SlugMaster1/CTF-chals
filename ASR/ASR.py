import socket
from Crypto.Util.number import bytes_to_long, getPrime
from Crypto.Util.Padding import pad
import os

FLAG = os.getenv('FLAG')

def genRSA():
    e = 3
    while True:
        p = getPrime(512)
        q = getPrime(512)
        phi = (p-1)*(q-1)
        if phi % e: break
    n = p * q
    d = pow(e, -1, phi)
    return (e, n, d)

def encrypt(m, n, d):
    if isinstance(m, str):
        m = m.encode()
    m = bytes_to_long(pad(m, 100))
    c = pow(m, d, n)
    return c

def handle_client(client_socket):
    e, n, d = genRSA()
    enc_flag = encrypt(FLAG.encode(), n, d)
    
    client_socket.sendall(f"Hello and welcome to my RSA encryption service!\n\nHere is your encrypted flag: {enc_flag}\n\n".encode())
    
    while True:
        client_socket.sendall(b"What would you like to encrypt?\n")
        
        data = client_socket.recv(1024).strip()
        if not data:
            break
        
        enc_data = encrypt(data.decode(), n, d)
        client_socket.sendall(f"Encrypted data: {enc_data}\n".encode())

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8000))
    server_socket.listen(5)

    while True:
        client_socket, addr = server_socket.accept()
        handle_client(client_socket)
        client_socket.close()

if __name__ == '__main__': main()