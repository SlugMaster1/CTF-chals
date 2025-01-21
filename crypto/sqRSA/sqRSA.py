from flag import FLAG
from Crypto.Util.number import getPrime, bytes_to_long
from Crypto.Util.Padding import pad

e = 2
p = getPrime(512)
q = getPrime(512)
n = p*q

print(f'{e = }')
print(f'{p = }')
print(f'{q = }')
print(f'{n = }')

m = bytes_to_long(pad(FLAG,100))
c = pow(m, e, n)

print(f'{c = }')

phi = (p-1)*(q-1)
d = pow(e,-1,phi)

print(f'{phi = }') # It always errors here?!!?!
print(f'{d = }')
