
xs = [0xb4,0xf7,0x39,0x59,0xea,0x39,0x4b,0x6b,0xbf,0x80,0x3d,0xd1,0x42,0x10,0xe4,0x42,0x105,0x58,0x15,0x108,0xab,0x18,0xe8,0xcd,0x1b,0xeb,0x51,0x1e,0x111,0x44,0x51,0x86,0x53,0x48,0x59,0x36,0x10a,0x9b,0xfd]
flag = ""

for i, x in enumerate(xs):
    found = False
    for c in range(0x20, 0x7f):
        if (((c & 0xF) << 4) | (c >> 4)) + i - x == 0:
            flag += chr(c)
            found = True
            break
    assert(found)
print(flag)
