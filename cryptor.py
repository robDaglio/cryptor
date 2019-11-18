from target import Target
from functions import check_args, get_target
from sys import argv

if __name__ == '__main__':

    encryption_pass = check_args()
    t = get_target()
    
    new_target = Target(argv[1], t, encryption_pass)
    new_target.file_ops()