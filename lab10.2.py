import os

def list_files_starting_with_f():
    for file in os.listdir():
        if file.startswith('f'):
            print(file)

list_files_starting_with_f()