import os
import subprocess
import string
import time




def is_in(parentlist, sublist):
  parentlist = parentlist.replace(" ","")
  sublist = sublist.replace(" ","")
  return sublist in parentlist

if __name__ == "__main__":
  wrong = 0
  start_time = time.time()
  flag = False
  for i in range(6):
    try:
      print i
      ans_f = open('./cnf/ans%d.txt'%i)
      ans = ans_f.read()
      if "unsatisfiable" in ans:
        a_unsat = True
      else:
        a_unsat = False
      result = subprocess.check_output('python main.py ./cnf/test%d.txt  --heuristic=firstLiteral'%i, shell=True)
      if "unsatisfiable" in result:
        r_unsat = True
      else:
        r_unsat = False
      if (a_unsat ^ r_unsat):
        wrong = wrong + 1
    except:
      wrong = wrong + 1
  end_time = time.time()
  if (wrong == 0):
    flag = True
  print "[PYGGI_RESULT] {runtime: %f,,pass_all: %s}"%(end_time-start_time,flag)
