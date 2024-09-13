# Tugas Besar Pengkom
import random
import pandas as pd
# program initialization

chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '(', ')', '*', '+']

seed = []
seed_dict = {}
pw_df = {}
initial_pw_df = pd.read_csv("C:/Users/Warge/OneDrive/Documents/Kuliah/pengkom/tubes/init_pw.csv").astype(object)

initial_pw = str(initial_pw_df.loc[0, "Init_pw"])

seed_df = pd.read_csv("C:/Users/Warge/OneDrive/Documents/Kuliah/pengkom/tubes/seeds.csv").astype(object)

all_passwords = [i for i in seed_df["Seeds"]]

all_passwords_name = [i for i in seed_df["Apps"]]

def password_generator(letter_l, letter_s, symbol, number, pass_type):
    '''Membuat password sesuai dengan keinginan user. Urutan diacak jika strong dan tidak diacak jika weak.'''

    password_list = []
    for char in range(letter_l):

        password_list.append(chars[random.randrange(0,26)])

    for char in range(letter_s):
        password_list.append(chars[random.randrange(26,52)])

    for char in range(number):
        password_list.append(chars[random.randrange(52,62)])
    for char in range(symbol):
        password_list.append(chars[random.randrange(62,71)])



    if pass_type == "a":
        random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    return password


# function pass_gen
def pass_gen():
    nr_letters_l = int(input("How many capital letters would you like? : "))
    nr_letters_s = int(input("How many small letters would you like? : "))
    nr_symbols = int(input("How many symbols would you like? : "))
    nr_numbers = int(input("How many numbers would you like? : "))
    types = input("Would you like your password to be (a) strong or (b) weak? (choose a or b) : ")
    index = 0
    password_array = []
    while True:
        print("Password Generated:")
        while index < 10:
            password_array.append(password_generator(nr_letters_l, nr_letters_s, nr_symbols, nr_numbers, types))
            index += 1

        j = 0
        for i in password_array:
            j += 1
            print(f"{j}. {i}")
        print("0. Regenerate Passwords")
        choice = int(input("Choose an option : ")) - 1
        if choice == -1:
            password_array.clear()
            index = 0
        else:
            print("Your final password is", password_array[choice])
            current_seed = ""
            for i in password_array[choice]:
                for j in chars:
                    if i == j:
                        if chars.index(i) < 10:
                            current_seed += "0"+str(chars.index(i))
                        else:
                            current_seed += str(chars.index(i))
            seed.append(current_seed)
            if input("Press 1 to change initial password and any key if not : ") == "1":
                initial_pw_df.loc[0] = str(seed[-1])
                initial_pw_df.to_csv("C:/Users/Warge/OneDrive/Documents/Kuliah/pengkom/tubes/init_pw.csv", index=False)
            else:
                all_passwords_name.append(input("What is it for? : ").upper())

                all_passwords.append(password_array[choice])

                seed_df.loc[len(seed_df.index)] = [all_passwords_name[-1],seed[-1]]

                seed_df.to_csv("C:/Users/Warge/OneDrive/Documents/Kuliah/pengkom/tubes/seeds.csv",index=False)

                print(f"Password for {all_passwords_name[len(all_passwords_name) - 1]} has been saved.")
            break

def decryptor(hash):

    hash = str(hash)
    decrypted = ""
    for i in range(0, len(hash)-1, 2):
        for j in range(len(chars)):
            if j >9:
                if str(hash[i]) + str(hash[i+1]) == str(j):
                    decrypted += chars[j]
            else:
                if str(hash[i]) + str(hash[i+1]) == "0" + str(j):
                    decrypted += chars[j]
    return decrypted



def main_menu():

    attempts = 1

    while True:
        if input("Input App password : ") == str(initial_pw):
            print("Welcome to PassGen Z Premium Ultimate Pro Max Plus Limited Edition")
            break
        elif attempts < 3:
            print("Wrong password {} attempts left".format(3 - attempts))
            attempts += 1
        else:
            print("Too many incorrect attempts")
            exit()

    while True:
        print("-------------------------------------------------------------------------------------------------------")
        print("1. Display All Passwords")
        print("2. Generate New Password")
        print("0. Exit")
        main_menu_option = int(input("Choose an option : "))
        if main_menu_option == 1 and (len(all_passwords) != 0):


            password_list_option()

        elif main_menu_option == 1:
            print("You have no passwords.")
        elif main_menu_option == 2:
            pass_gen()
        else:
            print("Thank you for using PassGen!")
            break


def password_list_option():
    all_passwords = [i for i in seed_df["Seeds"]]
    while len(all_passwords_name) != 0:
        print("-------------------------------------------------------------------------------------------------------")
        print("Password List")

        for i in range(len(all_passwords_name)):
            print(f"{i+1}. {all_passwords_name[i]} : {decryptor(all_passwords[i]) }")

        print("-------------------------------------------------------------------------------------------------------")
        print("1. Delete A password")
        print("0. Exit")
        password_list_option_choice = int(input("Choose an option : "))
        if password_list_option_choice == 1:
            delete_name = int(input("Choose which App/web index number password to delete : "))
            all_passwords.pop(delete_name - 1)
            all_passwords_name.pop(delete_name - 1)
            seed_df.drop([delete_name - 1] ,axis=0, inplace=True)
            seed_df.reset_index(drop=True)
            seed_df.to_csv("C:/Users/Warge/OneDrive/Documents/Kuliah/pengkom/tubes/seeds.csv", index=False)
            print(f"Password for {delete_name} has been successfully deleted.")
        else:
            break


#main program

if initial_pw != "12345":
    initial_pw = decryptor(initial_pw)


main_menu()
