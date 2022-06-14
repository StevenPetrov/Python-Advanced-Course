import os
from os.path import exists
# from os import mkdir
#
# directory = './'
# mkdir('./test')

file = './delete_me.txt'
try:
    os.remove(file)
except FileNotFoundError:
    print('File already deleted!')

# if exists(file):
#     os.remove(file)
# else:
#     print('File already deleted!')
