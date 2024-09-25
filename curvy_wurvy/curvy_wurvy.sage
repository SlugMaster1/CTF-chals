from Crypto.Util.number import bytes_to_long
from secret import FLAG, master_key

def Curve25519():
    p = 2^255-19
    E = EllipticCurve(GF(p),[0,486662,0,1,0])
    return p, E

def KDF(master_key, uid):
    user_key = master_key*uid + master_key//uid + uid
    return user_key

def sign(E, data, key):
    padding = 0
    while True:
        try:
            point = E.lift_x(data + padding)
            break
        except ValueError:
            padding += 1
    signed_point = point*key
    return signed_point.x() + (padding<<256)

def verify(E, data, signature, key):
    real_sig = sign(E, data, key)
    return real_sig == signature

def menu():
    print("What would you like to do?")
    print("1. Get user id")
    print("2. Sign data")
    print("3. Verify signature")
    while True:
        inp = input()
        if inp not in {'1','2','3'}:
            print(f"Invalid choice {inp}")
        else:
            return inp

def main():
    print("Welcome to my ECC data signing server!")
    p, E = Curve25519()
    flag_uid = randint(1, int(p^(1/4)))
    flag_key = KDF(master_key, flag_uid)
    flag_sig = sign(E, Integer(bytes_to_long(FLAG)), flag_key)
    print(f"Verify the true flag with\nUID: {flag_uid}\nSignature: {flag_sig}")
    while True:
        choice = menu()
        match choice:
            case '1':
                uid = randint(1, int(p^(1/4)))
                print(f"Your user id is: {uid}")
            case '2':
                try:
                    data = Integer(input(f"Enter your data: "))
                    uid = Integer(input(f"Enter your UID: "))
                except ValueError:
                    print("Please enter your data as an integer")
                    continue
                user_key = KDF(master_key, uid)
                sig = sign(E, data, user_key)
                if sig is None:
                    print("Your data does not fit within the bound of Curve25519")
                    continue
                print(f"Your signature is: {sig}")
            case '3':
                try:
                    data = Integer(input(f"Enter your data: "))
                    sig = Integer(input(f"Enter your signature: "))
                    uid = Integer(input(f"Enter your UID: "))
                except ValueError:
                    print("Please enter your data as an integer")
                    continue
                user_key = KDF(master_key, uid)
                if verify(E, data, sig, user_key):
                    print("Verified")
                else:
                    print("Verification Failed")
        print()
        
if __name__ == '__main__':
    main()