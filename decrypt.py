# A small tool to decrypt Naomi/Triforce/Chihiro images.
# (Actually, I tested this only with triforce images. You might need to tweak the
# key searching part for the other systems.)
#
# The tool relies on a key database, which can be downloaded from the Internet, for
# example from TheGuru's ROM Dump News page. 
# This tool will try all found keys, until it finds a matching one. This can be helpful,
# for example because many of the updat discs actually use keys from some other games.
#
# Have fun!
#
#  (c) 2008 tmbinc <tmbinc@elitedvb.net> 
#  http://debugmo.de
#
# Random thanks go out to:
# MrSporty, ElSemi, Serantes, TheGuru, BoboPJ64 for their individual contributions.

# You need pycrypto, who would have thought that...

from Crypto.Cipher import DES
import sys

if len(sys.argv) != 3:
	print "Usage: %s <main image file> <key-url>"
	exit()

def hex(string):
	return ' '.join(["%02x" % ord(x) for x in string])

def bin(string):
	res = ""
	for i in range(len(string)/2):
		res += chr(int(string[i*2:i*2+2], 0x10))
	return res

file = open(sys.argv[1], "rb")

def loadkeys(url):
	import urllib
	page = urllib.urlopen(url).read()
	import re
	return [bin(x) for x in re.findall("VER0001 .* .* .* ([0-9A-F]*)<", page)]

def findkey(file, keys):
	# find repeating pattern
	patterns = { }
	for i in range(1024):
		data = file.read(8)
		patterns.setdefault(data, 0)
		patterns[data] += 1

	# sort list
	patterns = [(i[1], i[0]) for i in patterns.items()]
	patterns.sort()

	# take highest hit
	print "assuming that %s will yield zeros when decrypted." % hex(patterns[-1][1])

	des = None
	pattern = patterns[-1][1][::-1]
	for key in keys:
		print(key)
		d = DES.new(key[::-1], DES.MODE_ECB)
		if d.decrypt(pattern) == "\0" * 8:
			return d, key

	return None, None

# Load keys
keys = loadkeys(sys.argv[2])

# find correct key
key = "CEA2131991982F2A".decode("hex")
des = DES.new(key[::-1], DES.MODE_ECB)
assert des is not None, "no key found :("

print "ok, found key %s" % hex(key)
outfile = open(sys.argv[1] + ".gcm", "wb")

# decrypt file
file.seek(0, 2)
l = file.tell()
file.seek(0)

while True:
	print "decrypting %08x/%08x (%d %%)\r" % (file.tell(), l, file.tell() * 100 / l), 
	data = file.read(1024*1024)[::-1]
	if not data:
		break
	data = des.decrypt(data)[::-1]
	outfile.write(data)
outfile.close()
