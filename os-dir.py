import os  #imports the OS
import sys

#Here is where the user is asked to enter names
folder_name = input('Enter a folder name: ')
file_name = input('Enter a file name: ')

#This should provide a message that tells user a file or folder already exists
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

#Tells user to type info
name = input('Please enter your name: \n')
address = input('Please enter your address: \n')
phone = input('Please eneter your phone number: \n')

#Opens as write and read with proper format.
with open(file_path, 'w+') as f:
    f.writelines(name + '\n')
    f.writelines(address + '\n')
    f.writelines(phone + '\n')