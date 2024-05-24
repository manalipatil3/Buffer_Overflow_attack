#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <source_file> <arg1> <arg2>"
    exit 1
fi

gcc -fno-stack-protector -z execstack -fno-pie -no-pie -m32 -O0 -g vuln_program.c -o vuln_program
echo ""
echo "***output for the first section of code---->***"
echo ""
python3 attack.py "$1"
./vuln_program < attack_string
echo ""
echo "***output for the second section of code---->***"
echo ""
python3 shellcode.py "$2"
setarch $(uname -m) -R ./vuln_program < shell_string

