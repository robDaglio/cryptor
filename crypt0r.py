#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Title: crypt0r
# Description: Recursive directory encryption tool
# Author: w15p
# Purpose: Educational
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#!/usr/bin/env python
import time, os, argparse, getpass, pyAesCrypt, progressbar, sys

BUFFER_SIZE = 64 * 1024

def get_args():
        
        global current_dir, operation
        
        parser = argparse.ArgumentParser()
        parser.add_argument('directory', type=str, default='', help='Directory path...')
        parser.add_argument('mode', type=str, default='', help='Mode [e or d]...')
        args = parser.parse_args()
        
        current_dir = args.directory
        operation = args.mode
        
        operation = operation.upper()

def get_files():
        
        global complete_paths
        
        complete_paths = []

        for root, subs, files in os.walk(current_dir):

                for f in files:
                        file_path = os.path.join(root, f)
                        complete_paths.append(file_path)

def encrypt():
        
        for item in complete_paths:
                
                file_name, file_extension = os.path.splitext(item)
                if file_extension != '.py':
                        pyAesCrypt.encryptFile(item, item + '.aes', password, BUFFER_SIZE)

def decrypt():
        
        for item in complete_paths:
                
                file_name, file_extension = os.path.splitext(item)
                if file_extension != '.py':
                        item = os.path.abspath(item)
                        pyAesCrypt.decryptFile(item, item.strip('.aes'), password, BUFFER_SIZE)
        
def delete_originals():
        
        for item in complete_paths:
                
                file_name, file_extension = os.path.splitext(item)
                if file_extension != '.py' and file_extension != '.aes':
                        os.remove(item)
                        
        
def delete_encrypted():
        
        for item in complete_paths:
                
                file_name, file_extension = os.path.splitext(item)
                if file_extension == '.aes': 
                        os.remove(item)

def progress_bar():
        
        bar = progressbar.ProgressBar()
        for b in bar(range(100)):
                time.sleep(.009)
                        
def run():
        
        global password, del_origs
        get_args()       
        
        while True: 
                if operation == 'E':
                        while True:
                                os.system('clear')
                                time.sleep(1)
                                password = getpass.getpass('[?] Key: ')
                                del_origs = input('[?] Delete original files? [y or n]: ')
                                
                                if del_origs == 'y':
                                        get_files()
                                        encrypt()
                                        delete_originals()
                                        
                                        print('[*] Encrypting...')
                                        progress_bar()
                                        time.sleep(1)                                        
                                        print('[*] Deleting originals...')
                                        progress_bar()
                                        print('[*] Done...')
                                        
                                        break
                                elif del_origs == 'n':
                                        get_files()
                                        encrypt()
                                        
                                        print('[*] Encrypting...')
                                        time.sleep(1)
                                        progress_bar()
                                        print('[*] Done...')
                                        
                                        break
                                else:
                                        print('[x] Please enter valid input...')
                elif operation == 'D':
                        while True:
                                os.system('clear')
                                time.sleep(1)
                                password = getpass.getpass('[?] Key: ')
                                del_enc = input('[?] Delete encrypted files? [y or n]: ')
                                
                                if del_enc == 'y':
                                        get_files()
                                        decrypt()
                                        delete_encrypted()
                                        
                                        print('[*] Decrypting...')
                                        progress_bar()
                                        time.sleep(1)                                        
                                        print('[*] Deleting encrypted files...')
                                        progress_bar()
                                        print('[*] Done...')                                        
                                        
                                        break
                                elif del_enc == 'n':
                                        get_files()
                                        decrypt()
                                        
                                        print('[*] Decrypting...')
                                        time.sleep(1)
                                        progress_bar()
                                        print('[*] Done...')                                        
                                        
                                        break
                                else:
                                        print('[x] Please enter valid input...')
                else:
                        print('[x] Invalid switch- exiting...')
                        break
                sys.exit(0)

def main():
                                
        run()
                
if __name__ == '__main__':
        main()
