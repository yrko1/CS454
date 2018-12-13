from pyggi import Program, Patch, GranularityLevel, TestResult
from pyggi.atomic_operator import StmtReplacement, StmtInsertion
from pyggi.custom_operator import StmtDeletion, StmtMoving
from pyggi.helper import stmt_python
import ast
import astor
import copy
import random

# Custom parser for the results of pytest
def result_parser(stdout, stderr):
    import re
    m = re.findall("runtime: ([0-9.]+)", stdout)
    if len(m) > 0:
        runtime = m[0]
        failed = re.findall("([0-9]+) failed", stdout)
        pass_all = len(failed) == 0
        return TestResult(True, {'runtime': runtime, 'pass_all': pass_all})
    
    else:
        return TestResult(False, None)

# Create new Program instance for 'sample/Triangle_fast_python'
triangle = Program(
    "sample/Triangle_fast_python", granularity_level=GranularityLevel.AST)
triangle.print_modification_points('triangle.py')

# Set modification weights
weights = [0.01] * len(triangle.modification_points['triangle.py'])
weights[7] = 1.0 # delay() 
triangle.set_modification_weights('triangle.py', weights)

# Create new Patch
patch = Patch(triangle)
valid_edit_operators = [StmtDeletion, StmtMoving, StmtReplacement]
edit_operator = random.choice(valid_edit_operators)
patch.add(edit_operator.create(triangle, method='weighted'))

# Print the patch's info, test results, and line differences made by the patch
print (patch)
print (patch.run_test(timeout=30, result_parser=result_parser))
print (patch.diff)
