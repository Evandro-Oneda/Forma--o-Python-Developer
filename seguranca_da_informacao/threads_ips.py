import ipaddress

ip = "192.168.0.1"

endereco = ipaddress.ip_address(ip)

print("ip: ", endereco + 256)

network = "192.168.0.0/24"

rede = ipaddress.ip_network(network, strict=False)

print("rede: ", rede)
for network in rede:
    print(network)
