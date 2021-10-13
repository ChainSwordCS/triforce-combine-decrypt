# triforce-combine-decrypt
Python scripts for combining and decrypting Triforce Arcade NAND Media Board games

For use with original MAME ROM dump format data (sometimes dumped directly with a chip Programmer).

Converts into a single decrypted ISO, playable with Dolphin-Triforce-Branch, Nintendont, QuadForce, etc.

decrypt.py can also be used with GD-ROM dumps, original instructions can be found here: https://web.archive.org/web/20140424035504/http://debugmo.de/2008/08/just-a-small-tool/

Original programs written by tmbinc, maybe with help from others.

# Credits

* tmbinc for the original program binary
* Eiim for the modified binary from ~2020
* ChainSwordCS for help with the project and small modifications to the programs

Random thanks go out to the following people for their individual contributions.

* MrSporty
* ElSemi
* Serantes
* TheGuru
* BoboPJ64

# Instructions

## combine.py

You must install Python 2.

Usage: `combine.py <input files - IC1.bin IC2.bin ..... IC9.bin etc> <output file>`

Example usage: `combine.py MKGP2_IC1.BIN MKGP2_IC2.BIN MKGP2_IC3S.bin MKGP2_IC4S.BIN MKGP2_IC5.BIN MKGP2_IC6.BIN MKGP2_IC7S.BIN MKGP2_IC8S.BIN MKGP2_IC9.BIN MKGP2_OUT.bin`

Tmbinc's original program would raise an exception when attempting to combine certain bad or malformed dumps, such as MAME's mkartag2 and mkartag2a. In the newest program, the error message is printed but the program continues combining the files anyway.

If your dump from your original media encounters this error, please try re-dumping it.

## decrypt.py

You must install Python 2 and pycrypto.

In the newest program, the usage is `decrypt.py <main image file> <key>` where `<key>` can be a key stored as plaintext in a file like key.bin, or it can just be plaintext input directly in the command.

In tmbinc's original program, the usage is `decrypt.py <main image file> <key-url>` where `<key-url>` was a URL to a website with a list of dumped encryption keys, such as "TheGuru's ROM Dump News page". That website may be offline, and it may not work from the original URL or from a web.archive.org URL, so we modified the program to accept any user-specified key as input.

The program will output a .GCM image file separate from the input file, which will not be overwritten. The .GCM file can later be renamed to .ISO as needed.

### Finding the encryption key

The key is possible to dump from original media, as shown by MrSporty here: https://www.youtube.com/watch?v=d8HEEAMlYIg (archive: https://web.archive.org/web/20211013195041/https://www.youtube.com/watch?v=d8HEEAMlYIg)

One could find a key online in a small number of places, including the aforementioned website (or its archive) and MAME on Github!

Helpful tip: often times, the key is the same between different regions of a given game, for example the Japanese and English versions of Mario Kart Arcade GP 2 share the same key. Additionally, "many of the update discs actually use keys from some other games". If one key doesn't work, keep trying multiple keys because another one may work instead.
