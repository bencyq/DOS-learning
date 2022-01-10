import os

with open('server.txt') as fp:
    texts = fp.read()
texts = texts.split('\n')
address = []
for text in texts:
    text = text.replace('\t', '').replace('N/A', '')
    text = text.split(' ')
    for i in range(text.count('')):
        text.remove('')
    address.append(text)
print(address)
servers = set()
os.system('chcp 65001')
for city in address:
    for server in city[1:]:
        p = os.popen(f'ping {server}')
        text = p.read()
        print(text)
        if text.count('timed out') <= 1 and text.count('find') == 0:
            servers.add(server)
        print(servers, len(servers))
print(servers)

with open('ping.txt','w') as fp:
    for server in servers:
        fp.write(server)
        fp.write('\r\n')

os.system("pause")