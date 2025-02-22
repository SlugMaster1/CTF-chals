#!/usr/local/bin/python
import json
import base64
from os import urandom
from hashlib import sha256
from datetime import datetime

N = urandom(32)
M = urandom(32)
END = int(datetime(2027, 6, 13, 13, 28, 17).timestamp())//(60*60*24) # The world ends at this time

def xor(plaintext, key, byteorder='big'):
    key = key*(len(plaintext)//len(key)) + key[:len(plaintext)%len(key)]
    int_pt = int.from_bytes(plaintext, byteorder)
    int_key = int.from_bytes(key, byteorder)
    int_enc = int_pt ^ int_key
    return int_enc.to_bytes(len(plaintext), byteorder)

def hash_exponentiation(secret, exponent):
    result = secret
    for _ in range(exponent):
        result = sha256(result).digest()
    return result

def timelock_encrypt(plaintext, time):
    key_n = hash_exponentiation(N, time)
    key_m = hash_exponentiation(M, END - time)
    key = xor(key_m, key_n)
    
    ciphertext = xor(plaintext, key)
    return ciphertext

def timelock_verify(plaintext, signature, time):
    ciphertext = timelock_encrypt(plaintext, time)
    true_signature = sha256(ciphertext).digest()
    return true_signature == signature

def timelock_sign(plaintext, time):
    ciphertext = timelock_encrypt(plaintext, time)
    signature = sha256(ciphertext).digest()
    return signature

def get_day():
    timestamp = datetime.now().timestamp()
    days = int(timestamp)//(60*60*24)
    return days

def menu():
    while True:
        print('What would you like to do?')
        print('1. Sign message')
        print('2. Verify message')
        print('3. Get keys')
        print('4. Exit')
        try:
            choice = int(input('> '))
            assert choice in range(1, 5)
            break
        except (ValueError, AssertionError):
            print('There was a problem with your input.')
    return choice

def main():
    print('Welcome to Timelock Signatures! A signature algorithm for OG fans only')
    while True:
        choice = menu()
        match choice:
            case 1:
                print('What would you like to sign?')
                try:
                    b64_message = input('> ')
                    message = base64.b64decode(b64_message)
                except:
                    print('An error occurred with your input')
                    continue
                time = get_day()
                signature = timelock_sign(message, time)
                signature_object = {'message': b64_message, 'signature': base64.b64encode(signature).decode(), 'time': time}
                print(json.dumps(signature_object))
            case 2:
                print('Enter your signature object as json')
                try:
                    signature_object = json.loads(input('> '))
                    message = base64.b64decode(signature_object['message'])
                    signature = base64.b64decode(signature_object['signature'])
                    time = int(signature_object['time'])
                except:
                    print('An error occurred with your input')
                    continue
                if timelock_verify(message, signature, time):
                    print('Your message is verified')
                    if message == b'GIMME FLAG!':
                        if time < 10000:
                            print('Wow you must be an OG fan!')
                            with open('flag.txt') as f:
                                flag = f.read()
                            print('You have earned this flag: ')
                            print(flag)
                        else:
                            print('Yeah... you are clearly just a bandwagon fan... sorry')
                else:
                    print('Verification failed')
            case 3:
                print('You want to do your own signatures? Do you not trust us? Fine, here they are!')
                time = get_day()
                key_n = hash_exponentiation(N, time)
                key_m = hash_exponentiation(M, END - time)
                print(f'Key N: {key_n.hex()}')
                print(f'Key M: {key_m.hex()}')
            case 4:
                print('Sorry to see you go')
                break
        print()

if __name__ == '__main__':
    main()