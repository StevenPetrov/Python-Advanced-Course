from io import open
import os
from os.path import exists

while True:
    line = input()
    if line == 'End':
        break
    line = line.split('-')
    command = line[0]
    file_name = line[1]

    if command == 'Create':
        with open(f'./{file_name}', 'w') as _:
            pass

    elif command == 'Add':
        text = line[2]
        try:
            with open(f'./{file_name}', 'a') as file:
                file.write(text + '\n')
        except FileNotFoundError:
            with open(f'./{file_name}', 'w') as file:
                file.write(text + '\n')

    elif command == 'Replace':
        old_text, new_text = line[2], line[3]
        if exists(f'./{file_name}'):
            with open(f'./{file_name}', 'r+') as file:
                file_content = file.read().replace(old_text, new_text)
                file.seek(0)
                file.truncate(0)
                file.write(file_content)
        else:
            print("An error occurred")

    elif command == 'Delete':
        try:
            os.remove(f'./{file_name}')
        except FileNotFoundError:
            print("An error occurred")

# commands
# Create-file.txt
# Add-file.txt-First Line
# Add-file.txt-Second Line
# Replace-random.txt-Some-some
# Replace-file.txt-First-1st
# Replace-file.txt-Second-2nd
# Delete-random.txt
# Delete-file.txt
# End
