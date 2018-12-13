import os
import subprocess
import string
import time



if __name__ == "__main__":
  wrong = 0
  #start_time = time.time()
  flag = False
  N=100
  energy_avg = 0
  for j in range(N):
    energy = 0
    for i in range(6):
      try:
        ans_f = open('./cnf/ans%d.txt'%i)
        ans = ans_f.read()
        if "unsatisfiable" in ans:
          a_unsat = True
        else:
          a_unsat = False
        result = subprocess.check_output('./a.out python main.py ./cnf/test%d.txt  --heuristic=firstLiteral'%i, shell=True)
        if "unsatisfiable" in result:
          r_unsat = True
        else:
          r_unsat = False
        if (a_unsat ^ r_unsat):
          wrong = wrong + 1
      except:
        wrong = wrong + 1

      result = str(result)
      split_result = result.split("()")[-1]
      energy = energy + float(split_result.split('\\')[1].split('n')[-1])

    energy_avg= energy_avg + energy
    #end_time = time.time()
  energy_avg= energy_avg/N


  if (wrong == 0):
    flag = True
  print ("[PYGGI_RESULT] {runtime: %f,,pass_all: %s}"%(energy_avg,flag))
  
  #print "[PYGGI_RESULT] {runtime: %f,,pass_all: %s}"%(,flag)
