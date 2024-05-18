import os
import hashlib

db = ['']

def check(signature, efile):
    print(f"  {signature}  ")
    if signature in db:
        print(f"  Malicious{efile}  ")
        
file_list = os.listdir(".")
for efile in file_list:
    if ".exe" in efile:
        result = hashlib.md5(efile.encode())
        signature = result.hexdigest()
        check(signature, efile)