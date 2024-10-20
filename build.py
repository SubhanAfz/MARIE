import sys
from parser import Parser

file_name = sys.argv[1]

try:
    memory_name = sys.argv[2]
    Parser(open(f'{file_name}', 'r'), memory_name)
except IndexError:
    Parser(open(f'{file_name}', 'r'))
