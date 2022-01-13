import os
import threading

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
servers = []
for city in address:
    for server in city:
        if '.com' in server:
            servers.append(server)

print(servers)
ping = set()


class myThread(threading.Thread):
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print("开启线程： " + self.name)
        while len(servers) > 0:
            available = 0
            # 获取锁，用于线程同步
            threadLock.acquire()
            server = acquire_server()
            # 释放锁，开启下一个线程
            threadLock.release()
            os.system('chcp 65001')
            p = os.popen(f'ping {server}')
            text = p.read()
            if text.count('timed out') <= 1 and text.count('find') == 0:
                ping.add(server)
                available = 1
            threadLock.acquire()
            print(self.name, server, available)
            threadLock.release()


def acquire_server():
    return servers.pop()


threadLock = threading.Lock()  # 定义线程锁

# 创建新线程
threads = {'thread' + str(i): myThread(i, 'thread' + str(i), 0) for i in range(20)}

# 开启新线程
for value in threads.values():
    value.start()

# 等待所有线程完成
for t in threads.values():
    t.join()
print("退出主线程")
print(ping)
with open('ping.txt','w') as fp:
    for p in ping:
        fp.write(p)
        fp.write('\r\n')

os.system("pause")