### Manali Patil
### B-Number :- B01035189
### Programming Language : python

### Run the code using Make.sh

Command :- ./make.sh $arg0{this is target function address} $arg1{shellcode file}

for instance:-

******mpatil3@remote02:~/CS$./make.sh 08049196 shellcode*

### Note :-
if get below error for make.sh file while running :-

mpatil3@remote02:~/CS/bkp/proj1_mpatil3/proj1_mpatil3$ ./make.sh
bash: ./make.sh: Permission denied

Run below command

command :-chmod +x make.sh

for example:-
mpatil3@remote02:~/CS/bkp/proj1_mpatil3/proj1_mpatil3$ chmod +x make.sh
mpatil3@remote02:~/CS/bkp/proj1_mpatil3/proj1_mpatil3$./make.sh 08049196 shellcode

### Run withous using make.sh

commands:-
gcc -fno-stack-protector -z execstack -fno-pie -no-pie -m32 -O0 -g vuln_program.c -o vuln_program

## to check section 1 output
python3 attack.py 08049196
./vuln_program < attack_string

## to check section 2(bonus) output
python3 shellcode.py shellcode
setarch $(uname -m) -R ./vuln_program < shell_string



### Status :- Complete (both the section)

### Test cases :-

log:-
mpatil3@remote02:~/CS/proj3$ ./make.sh 08049196 shellcode
vuln_program.c: In function ‘prompt’:
vuln_program.c:15:9: warning: implicit declaration of function ‘gets’; did you mean ‘fgets’? [-Wimplicit-function-declaration]
   15 |         gets(buf);
      |         ^~~~
      |         fgets
/usr/bin/ld: /tmp/ccBkfGQD.o: in function `prompt':
/home/mpatil3/CS/proj3/vuln_program.c:15: warning: the `gets' function is dangerous and should not be used.

***output for the first section of code---->***

***Output file 'attack_string' created successfully.***

You have entered the correct passwd

***output for the second section of code---->***

Output file 'shell_string' created successfully.
$ exit
 
