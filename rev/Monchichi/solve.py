from Crypto.Util.number import long_to_bytes
def bswap(num):
    return (num&0xff)<<24|(num&0xff00)<<8|(num&0xff0000)>>8|(num&0xff000000)>>24

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ciphertext = 'FPGNIOYLAHGUGYJZDDTTVXOFTLVIXMWLQDNWUFTRUSHHZUTJOTOYZEBKQGJLYAQPYKWKPDAUQDIFACYIRNOTKRDKB'
ct = 0
for c in ciphertext[::-1]:
    ct *= 26
    ct += alphabet.index(c)
count = 0
while count + count.bit_length() < ct.bit_length():
    ct ^= count<<count
    count += 1
ct = int(bin(ct)[-1:1:-1],2)
count = 0
pt = 0
while ct:
    pt |= bswap(ct&0xffffffff)<<count*32
    ct >>= 32
    count += 1
print(long_to_bytes(pt).decode())
