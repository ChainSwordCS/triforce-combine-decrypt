import os, sys, struct

fs = [open(x, "rb") for x in sys.argv[1:9]]
blockmap = struct.unpack("<262144H", open(sys.argv[9], "rb").read())

out = open(sys.argv[10], "wb")

def hexs(string):
	return ' '.join(["%02x" % ord(x) for x in string])

ind = 0
import sys

for i in blockmap:
	if i == 65535:
		break

	real_pos = i * 0x4000
	
	block = real_pos / (64*1024*1024)
	f = fs[block*2:block*2+2]
	real_pos -= block * (64*1024*1024)
	
	f[0].seek(real_pos / 0x200 * 0x210)
	f[1].seek(real_pos / 0x200 * 0x210)
	
	for j in range(0x4000/0x200):
		r1 = f[0].read(0x200)
		r2 = f[1].read(0x200)
		s1 = f[0].read(0x10)
		s2 = f[1].read(0x10)
		if len(r1) != 0x200:
			raise Exception("illegal pos! %08x %02x" % (real_pos, i))
		res = ''.join(r1[i] + r2[i] for i in range(0x200))
		out.write(res)
		if not (ind & 0xFFFF):
			sys.stdout.flush()
			print "\r" + hex(ind),
		ind += 0x200
