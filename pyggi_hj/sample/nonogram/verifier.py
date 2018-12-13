import os
import subprocess
import string
import time
import pytest



def is_in(parentlist, sublist):
    parentlist = parentlist.replace(" ","")
    sublist = sublist.replace(" ","")
    return sublist in parentlist

if __name__ == "__main__":
    wrong = 0
    start_time = time.time()
    flag = False
    for i in range(12):
        try:
            ans_f = open('ans%d.txt'%i)
            ans = ans_f.read()
            result = subprocess.check_output('python nonogram.py test%d.txt'%i, shell=True)
            if not is_in(result,ans):
                wrong = wrong + 1
        except:
            wrong = wrong + 1
    if (wrong == 0):
        flag = True
#print(time.time())
print("[PYGGI_RESULT] {runtime: %f,pass_all: %s}"%(time.time() - start_time,flag))
#print("[PYGGI_RESULT] {runtime: "+str(run_time)+)
