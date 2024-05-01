# Nome: Thiago F. Santos

import socket
import requests

listValidIp = []

listSubdomains = requests.get('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-top1million-5000.txt')

listDomain = ['uniftec.com.br', 'ftec.com.br']

urlIp = 'https://rdap.registro.com.br/ip/'

for domain in listDomain:
    for sub in listSubdomains.text.split('\n'):
        try:
            ip = socket.gethostbyname(f'{sub}.{domain}')
            print(f'- O subdominio {sub}.{domain} e o seu endereço ip - {ip}')

            response = requests.get(f'{urlIp}{ip}')
            validIp = response.json()['handle']

            if validIp not in listValidIp:
                listValidIp.append(validIp)

        except Exception:
            pass        

print(listValidIp)