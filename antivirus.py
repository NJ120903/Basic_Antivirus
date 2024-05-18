import os
import hashlib

#if you want to use your own database
#db = ['']

#if File is provided
with open('bases.cav', 'r') as file:
    db = [line.strip() for line in file]

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
