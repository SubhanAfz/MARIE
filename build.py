import sys
from parser import Parser

file_name = sys.argv[1]

Parser(open(f'{file_name}', 'r'))