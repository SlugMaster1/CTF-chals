import random
from secret import FLAG

def seed(user_seed):
    flag = int.from_bytes(FLAG,"big")
    new_seed = flag % user_seed
    random.seed(new_seed)

def main():
    print("Welcome to my very secure RNG, please choose an option:")
    while True:
        print("1. Input new seed")
        print("2. Get random")
        choice = input()
        if choice.strip() == '1':
            try:
                inp = int(input("Enter your new seed: "))
            except ValueError:
                print("Please enter an integer")
                continue
            if inp > 200 or inp < 1:
                print("Your seed must be between 1 and 200")
            seed(inp)
        elif choice.strip() == '2':
            print(random.randint(0,0xffffffff))
        else:
            print(f"'{choice}' is not a recognized option")

if __name__ == '__main__':
    main()