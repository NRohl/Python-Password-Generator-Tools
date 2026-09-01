import secrets
import os 

def get_words_dictionary():
    # See https://github.com/dwyl/english-words/blob/master/words_alpha.txt
    clean_words = []
    with open("words_alpha.txt") as words_file:
        for word in words_file.readlines():
            clean_words.append(''.join(s for s in word if ord(s)>31 and ord(s)<126))
        return len(clean_words) , clean_words
def generate_password():
    num_words = int(input("How many words do you want to have in the password? (int) "))
    special_characters = input("Convert letters to special characters? Y/n ")
    if special_characters.lower() == "y":
        special_characters_chance = float(input("Bias to convert letters with special character look alikes to special characters? (float 0.0 to 1.0) "))
    else:
        special_characters_chance = 0.0
    special_characters_two = input("Add special characters to the end? Y/n ")
    if special_characters_two.lower() == "y":
        special_characters_two_count = int(input("Number of special characters to add the end? (int) "))
    else:
        special_characters_two_count = 0
    numbers = input("Add numbers characters to the end? Y/n ")
    if numbers.lower() == "y":
        numbers_at_end = int(input("How many numbers should be at the end of the password? (int) "))
    else:
        numbers_at_end = 0
    password = ""
    dictionary_length, dictionary = get_words_dictionary()
    special_list_characters = [["@","4"],["$"],["!","1","|"],["0"],["!","1","|"],["3"]]
    special_characters_list = ["a","s","i","o","l","e"]
    special_list_characters_all = ["`","~",'!',"@","#","$","%","^","&","*","(",")","-","_",'+','=',"[","]","{","}",";",":","'",'"',",","<",">",".","/","?"]
    for i in range(num_words):
        password += secrets.choice(dictionary)
    for i in range(len(password)):
        if secrets.randbelow(10) > 5:
            password = password[:i] + password[i].upper() + password[i+1:]
    for i in range(numbers_at_end):
        password += str(secrets.randbelow(10))
    for i in range(special_characters_two_count):
         password += secrets.choice(special_list_characters_all)
    for i in range(len(password)):
        if password[i] in special_characters_list:
            index = special_characters_list.index(password[i])
            if secrets.randbelow(100) <= special_characters_chance * 100:
                password = password[:i] + secrets.choice(special_list_characters[index]) + password[i+1:]
    return(password)
def ask_quit():
    choice = input("Quit? Y/n")
    if choice.lower() == "y" or choice.lower() == "n":
        if choice.lower() == "y":
            pass
        elif choice.lower() == "n":
            ask_gen_pass()
    else:
        print("Response improperly formatted.")
        ask_quit()
def ask_gen_pass():
    choice = input("Do you want to generate a password? Y/n")
    if choice.lower() == "y" or choice.lower() == "n":
        if choice.lower() == "y":
            print(generate_password())
        else:
            ask_quit()
    else:
        print("Response improperly formatted.")
        ask_gen_pass()
def main():
    os.chdir("C:\\projects\\Python\\")
    print("Loading secure password generator . . .")
    ask_gen_pass()
if __name__ == "__main__":
    main()
