import struct, os
Game = '黄昏のフォルクローレ'
cn = './14b\\'
if not os.path.exists(cn):
    os.mkdir(cn)
files = os.listdir(cn)
filecont = len(files)
f = open('data01110.arc', 'wb')
f.write(b'BURIKO ARC20')
f.write(struct.pack('i', filecont))
pos = 0
data = b''
fileheader = b'DSC FORMAT 1.00\x00'
fileheader=b''
for file in files:
    size = os.stat(cn + file).st_size
    data = data + struct.pack(f'{96}s', file.encode('cp932'))
    data = data + struct.pack('i', pos)
    data = data + struct.pack('i', size)
    data = data + struct.pack(f'{24}s', ''.encode('cp932'))
    pos = pos + size + len(fileheader)
pos = 0
for b in data:
    b = b#(b - key[pos % len(key)]) & 0xFF
    pos = pos + 1
    b = struct.pack('B', b)
    f.write(b)
for file in files:
    f1 = open(cn + file, 'rb')
    b = f1.read()
    f1.close()
    f.write(fileheader)
    f.write(b)
f.close()
