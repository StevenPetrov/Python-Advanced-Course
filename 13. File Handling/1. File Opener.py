import os
from io import open
try:
    file = open('./text.txt')
    print('File found')
except FileNotFoundError:
    print('File not found')

