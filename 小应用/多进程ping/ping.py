import subprocess

p = subprocess.Popen('ping www.baidu.com', shell=True, stdout=subprocess.PIPE)
print(p.poll())
print(p.wait())
print(p.stdout.read().decode('gbk'))

print(p.kill())

