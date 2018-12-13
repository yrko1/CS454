"""
Improving non-functional properties ::

    python improve_python.py ../sample/Triangle_fast_python
"""
import sys
import random
import argparse
from pyggi import Program, Patch, GranularityLevel, TestResult
from pyggi.algorithms import LocalSearch
from pyggi.atomic_operator import LineReplacement, LineInsertion
from pyggi.custom_operator import LineDeletion

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='PYGGI Improvment Example')
    parser.add_argument('project_path', type=str, default='../sample/Triangle_fast_python')
    parser.add_argument('--epoch', type=int, default=30,
        help='total epoch(default: 30)')
    parser.add_argument('--iter', type=int, default=100,
        help='total iterations per epoch(default: 100)')
    args = parser.parse_args()
    
    program = Program(args.project_path, GranularityLevel.AST)
    program.print_modification_points('triangle.py')
