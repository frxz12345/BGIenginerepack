import struct, os

cn = './cn\\'
if not os.path.exists(cn):
    os.mkdir(cn)
files = os.listdir(cn)
filecont = len(files)
f = open('data02500.arc', 'wb')
f.write(b'PackFile    ')
f.write(struct.pack('i', filecont))
pos = 0
data = b''
for file in files:
    size = os.stat(cn + file).st_size
    nl = len(file.encode('CP932'))
    null = (16 - nl) * b'\x00'
    data = data + file.encode('cp932')
    data = data + null
    data = data + struct.pack('i', pos)
    data = data + struct.pack('i', size)
    data = data + struct.pack('i', 0)*2
    pos = pos + size + 0
f.write(data)
for file in files:
    f1 = open(cn + file, 'rb')
    b = f1.read()
    f1.close()
    # f.write(b'DSC FORMAT 1.00')
    # f.write(b'\x00')
    f.write(b)
f.close()
