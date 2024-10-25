import os
import time

with open("hosts.txt") as file:
    arquivo = file.read()
    arquivo = arquivo.splitlines()
    print(arquivo)

    for ip in arquivo:
        print(f"Verificando o IP: {ip}")
        print(" \n ######################################################\n")
        os.system(f"ping -n  5 {ip}")
        print(" \n ######################################################\n")
        time.sleep(5)


        

   