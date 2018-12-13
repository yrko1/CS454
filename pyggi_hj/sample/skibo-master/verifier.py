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
  energy_avg=0
  original_energy = 0

  N=10
  for j in range(N):
  	for i in range(6):
  		energy=0
  		try:
  			ans_f = open('./cnf/ans%d.txt'%i)
  			ans = ans_f.read()
  			if "unsatisfiable" in ans:
  				a_unsat = True
  			else:
  				a_unsat = False
  			result = subprocess.check_output('python main.py ./cnf/test%d.txt  --pure --unit  --heuristic=firstLiteral'%i, shell=True)
  			if "unsatisfiable" in result:
  				r_unsat = True
  			else:
  				r_unsat = False
  			if (a_unsat ^ r_unsat):
  				wrong = wrong + 1
  		except:
  			wrong = wrong + 1
		result = str(result)
		#split_result = result.split("()")[-1]
		#energy = energy + float(split_result.split('\\')[1].split('n')[-1])
  		#energy_avg= energy_avg + float(split_result.strip())
  end_time = time.time()
  #energy_avg= energy_avg/N
  #print(energy_avg)
  #fit_V = 3.268362/energy_avg
  #print(fit_V)
  if (wrong == 0):
    flag = True
  print ("[PYGGI_RESULT] {runtime: %f,,pass_all: %s}"%(end_time-start_time,flag))
