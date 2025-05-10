import struct, os

cn = './CN\\'
if not os.path.exists(cn):
    os.mkdir(cn)
key = key.encode('CP932')
files = os.listdir(cn)
filecont = len(files)
f = open('data01110.arc', 'wb')
f.write(b'BURIKO ARC20')
f.write(struct.pack('i', filecont))
pos = 0
data = b''
for file in files:
    size = os.stat(cn + file).st_size
    nl = len(file.encode('CP932'))
    null = (96 - nl) * b'\x00'
    data = data + file.encode('cp932')
    data = data + null
    data = data + struct.pack('i', pos)
    data = data + struct.pack('i', size)
    data = data + struct.pack('i', 0)*6
    pos = pos + size + 16
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
    f.write(b'DSC FORMAT 1.00')
    f.write(b'\x00')
    f.write(b)
f.close()
