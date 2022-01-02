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
servers = []
fp = open('ping.txt', 'w', encoding='utf-8')
for city in address:
    for server in city[1:]:
        p = os.popen(f'ping {server}')
        text = p.read()
        print(text)
        if text.count('请求超时') <= 1:
            servers.append(server)
        print(servers, len(servers))
print(servers)
