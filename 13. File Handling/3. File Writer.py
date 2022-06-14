from io import open


file = open('./my_first_file.txt', 'w')
file.write('I just created my first file!')
file.close()