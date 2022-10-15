import time
import os
import sys

def read_file(file):
    with open(file, 'r') as f:
        for line in f:
            check_name_format(line)

def check_name_format(full_name):
    name = ''.join([n for n in full_name if n == ' ' or n.isalpha()])
    # print(name)
    name = name.lower().split(" ")

    if len(name) == 2:
        create_username(name)

user_name = []

def create_username(name):
    first_name = name[0]
    last_name = name[1]

    # Format 1 :- flastname
    user_name.append(f"{first_name[0]+last_name}")

    # Format 2 :- f.lastname
    user_name.append(f"{first_name[0]}.{last_name}")


    # Format 3 :- f_lastname
    user_name.append(f"{first_name[0]}_{last_name}")


    # Format 4 :- firstname+l
    user_name.append(f"{first_name}{last_name[0]}")

    # Format 5 :- firstname_lastname
    user_name.append(f"{first_name}_{last_name}")

    
    # Format 6 :- firstname.lastname
    user_name.append(f"{first_name}.{last_name}")

    # Format 7 :- lastname.firstname
    user_name.append(f"{last_name}.{last_name}")
    
    # Format 8 :- l.firstname
    user_name.append(f"{last_name[0]}.{first_name}")

    # Format 9 :- firstname
    user_name.append(f"{first_name}")

    # Format 10 :- lastname
    user_name.append(f"{last_name}")

def print_intro():
    print("")
    print("--------------------------------------------------------")
    print("                    USERNAME GENERATOR")
    print("                       by enum3rat3")
    print("--------------------------------------------------------")

if __name__ == "__main__":
    print_intro()

    if len(sys.argv) !=2:
        print(f"[-] usage :- name_generator.py name_list\nname_list file must be in format: first_name<space>last_name")

    elif not os.path.exists(sys.argv[1]):
        print(f"File \"{sys.argv[1]}\" not found in {os.getcwd()}")

    elif os.path.isdir(sys.argv[1]):
        print(f"{sys.argv[1]} is a directory")

    else:
        read_file(sys.argv[1])

    for name in user_name:
        print(name)
