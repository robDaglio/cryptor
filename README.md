# cryptor
*** CAUTION: THIS PROGRAM CAN CAUSE IRREVERSIBLE DAMAGE IF MISUSED ***

This is essentially an AES256 implementation, utilizing the pyAesCrypt library for Python 3.6+

It can encrypt single files, or recursively encrypt entire directories. Should be used with caution, as it will not warn against encrypting essential system files. Please use with care and discretion.

The included binary has been compiled on Manjaro 18 5.3.11-1 on Python 3.7.4

Binary Usage: 

./cryptor <mode [-e or -d]> <FILE/DIR> <password (OPTIONAL) [-p]> <password>

Python Script Usage:

python cryptor <mode [-e or -d]> <FILE/DIR> <password (OPTIONAL) [-p]> <password>


