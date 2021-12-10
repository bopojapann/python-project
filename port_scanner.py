import socket
from IPy import IP


import tkinter
def scan(target):
    converted_ip = zemi_ip(target)
    print("\n"+"[-_0] Scaning target:" + str(target))
    for port in range(1, 85):
        scan_port(converted_ip, port)

#Funkcija so koja ja najduvam IP adresata!
def zemi_ip(ip):
    try:
        IP(ip)
        return(ip)
    except:
        return socket.gethostbyname(ip)

def get_baner(s):
    return s.recv(1024)

#Skenirajne dali nekoj port e otvoren ili ne
def scan_port(ipp, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((ipp, port))
        try:
            baner = get_baner(sock)
            print(f"[+] Open port:{port} baner: {str(baner.decode)}")
        except:
            pass
        print(f"[+] Port {port} is Open\n")
    except:
        pass
targets = input("Vnesi ja ip adresata ili adresite razdvoj so (,):")

if "," in targets:
    for ip_add in targets.split(","):
        scan(ip_add.strip(" "))
else:
    scan(targets)
