import subprocess
import sys
import itertools

sys.setrecursionlimit(10000)

class form:

    def __init__(self):
        self.left = None
        self.right = None
        self.op = None
        self.no = 0
        self.char = None
        self.p = None

    def __str__(self):
        if self.char != None:
            if self.no % 2 == 0:
                return str(self.char)
            else:
                return '- ' + str(self.char)
        elif self.no % 2 == 0:
            return '( %s %s %s )' %(self.left, self.op, self.right)
        else:
            return '( - %s %s %s )' %(self.left, self.op, self.right)

filename = sys.argv[1]

f = open('%s'%filename,'r')
#inp = open('./input.in','w')

col_num = int(f.readline())
row_num = int(f.readline())

rows = []
cols = []

fixed_points = []

variable_num = row_num*col_num + 1

for x in range(col_num):
    tmp = f.readline().split(" ")
    for y in range(len(tmp)):
        tmp[y] = int(tmp[y])
    rows.append(tmp)

for x in range(row_num):
    tmp = f.readline().split(" ")
    for y in range(len(tmp)):
        tmp[y] = int(tmp[y])
    cols.append(tmp)

def make_permutations(x,row_flag):
    if row_flag == True:
        line = rows[x]
    else:
        line = cols[x]
    blacks = 0
    for n in line:
        blacks += (n-1)
    if row_flag:
        availables = row_num - (len(line)-1) - blacks
    else:
        availables = col_num - (len(line)-1) - blacks
    comb_ = list(itertools.combinations(range(availables), len(line)))
    comb = []
    if row_flag:
        for possible in comb_:
            tmp = []
            for elem in range(len(possible)):
                te = possible[elem] + elem
                for y in range(elem):
                    te += line[y] - 1
                for y in range(line[elem]):
                    te += 1
                    tmp.append(te)
            comb.append(tmp)
    else:
        for possible in comb_:
            tmp = []
            for elem in range(len(possible)):
                te = (possible[elem] + elem - 1)*row_num + x + 1
                for y in range(elem):
                    te += (line[y] - 1)*row_num
                for y in range(line[elem]):
                    te += row_num
                    tmp.append(te)
            comb.append(tmp)

    if row_flag:
        for i in range(len(comb)):
            for j in range(len(comb[i])):
                comb[i][j] += row_num*x
    return comb

def gen_conj(cons, tmp_list):
    tmp = form()
    if len(tmp_list) == 1:
        if tmp_list[0] in cons:
            tmp.char = str(tmp_list[0])
        else:
            tmp.char = '-' + str(tmp_list[0])
        return tmp
    tmp.op = '&'
    tmp.left = gen_conj(cons, tmp_list[:1])
    tmp.right = gen_conj(cons, tmp_list[1:])
    return tmp

def make_dnf(comb, row_flag, l):
    if row_flag:
        tmp_list = range(1+l*row_num,1+l*row_num+row_num)
    else:
        tmp_list = range(1+l,1+row_num*col_num,row_num)
    tmp = form()
    if len(comb) == 1:
        tmp = gen_conj(comb[0],tmp_list)
        return tmp
    if len(comb) == 2:
        tmp.left = gen_conj(comb[0],tmp_list)
        tmp.right = gen_conj(comb[1],tmp_list)
        tmp.op = '|'
        return tmp
    tmp.op = '|'
    tmp.left = gen_conj(comb[0],tmp_list)
    tmp.right = make_dnf(comb[1:],row_flag,l)
    return tmp

def get_ands(f):
    ands = []
    if f.op == '|':
        l = get_ands(f.left)
        r = get_ands(f.right)
        if l == None or l == []:
            pass
        elif type(l[0]) == type([]):
            ands += l
        else:
            ands.append(l)
        if r == None or r == []:
            pass
        elif type(r[0]) == type([]):
            ands += r
        else:
            ands.append(r)
    elif f.op == '&':
        l = get_ands(f.left)
        r = get_ands(f.right)
        if f.left.char != None:
            if f.left.no == 1:
                ands.append("-"+f.left.char)
            else:
                ands.append(f.left.char)
        elif f.left.op == '&':
            ands += l
        else:
            print "ERROR!"
        if f.right.char != None:
            if f.right.no == 1:
                ands.append("-"+f.right.char)
            else:
                ands.append(f.right.char)
        elif f.right.op == '&':
            ands += r
        else:
            print "ERROR!"
    else:
        ands.append(f.char)
    return ands



def write_to_file():
    f = open('test.in','w')
    dummy = open('dummy','r')
    f.write('p cnf %d %d\n'%(variable_num-1, clauses))
    line = dummy.readline()
    while line:
        f.write(line)
        line = dummy.readline()

    f.close()
    dummy.close()

def print_output():
    f = open('test.out','r')
    f.readline()
    output = f.readline()
    output = output.split(' ')
    for y in range(col_num):
        for x in range(row_num):
            if output[y*row_num+x] == str(y*row_num+x+1):
                print '#',
            else:
                print '.',
                '''
            if '-'+str(y*row_num + x) in output:
                print '.',
            else:
                print '#',
                '''
        print ''

row_comb = []
col_comb = []


for x in range(col_num):
    row_comb.append(make_permutations(x,True))


for y in range(row_num):
    col_comb.append(make_permutations(y,False))


all_lines = []

clauses = 0

for i in range(col_num):
    c = make_dnf(row_comb[i], True, i)
    ands = get_ands(c)
    all_lines.append(ands)

for i in range(row_num):
    c = make_dnf(col_comb[i], False, i)
    ands = get_ands(c)
    all_lines.append(ands)


print all_lines

'''

write_to_file()

subprocess.call('minisat test.in test.out', shell=True)

print_output()
'''
