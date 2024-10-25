import os

ip_ou_host = input("Digite o ip ou ou host: ")

# os.system('ping -n 6 {}'.format(ip_ou_host))
os.system(f'ping -n 1000 {ip_ou_host}')