import os
import sys

folder_name = input('Enter a folder name: ')
file_name = input('Enter a file name: ')

folder_path = folder_name
if not os.path.exists(folder_path):
    try:
        os.makedirs(folder_path)
    except FileExistsError:
        print(folder_name, 'already exist.')

file_path = file_name
if not os.path.exists(os.path.join(folder_name, folder_path)):
    try:
        os.makedirs(os.path.join(folder_path, file_path +'.txt'))
    except FileExistsError:
        print(file_name, 'already exists!')

name = input('Please enter your name: \n')
address = input('Please enter your address: \n')
phone = input('Please eneter your phone number: \n')

with open(file_path, 'w+') as f:
    f.writelines(name + '\n')
    f.writelines(address + '\n')
    f.writelines(phone + '\n')