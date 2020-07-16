from sys import argv, exit
from getpass import getpass
import os

def usage():
    print(f'[!] Usage: python {argv[0]} <mode [-e or -d]> <FILE/DIR> <password (OPTIONAL) [-p]> <password>')

def check_args():
    if len(argv) == 1 or len(argv) == 2 or len(argv) == 4:
        usage()
        exit(0)

    if (argv[1] == "-d" or argv[1] == "-e") and os.path.exists(argv[2]):
        pass
    else:
        usage()
        exit(0)

    if (len(argv) == 3):
        return getpass("[!] Password: ")
    elif (len(argv) == 5):
        return get_pass()
    else:
        usage()
        exit(0)    

def get_target():
    if os.path.isdir(argv[2]):
        file_names = list()
        for root, dirs, files in os.walk(os.path.abspath(argv[2])):
            for f in files:
                file_names.append(os.path.join(root, f))
        return file_names
    else:
        return os.path.abspath(argv[2])

def get_pass():
    if argv[3] == '-p':
        return argv[4]
    else:
        print('[x] Invalid switch!')
        usage()
        exit(0)