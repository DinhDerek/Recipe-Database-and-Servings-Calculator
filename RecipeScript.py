import csv
from add_recipe import add_recipe


def create_csv(csv_file):
    while True:
        try:
            new_csv = open(csv_file, mode='w+')
            new_csv.close()
            print("New .csv file successfully created.\n")
            break
        except:
            print("Invalid character found in the file name, please try again.\n")
            csv_file = input("Please enter a name for the new .csv file.\n> ")
            pass


print("[Not sure what to put as the welcome text yet]")
while True:
    csv_file = input("Please enter a .csv file to begin (\"quit\" to quit the program):\n> ")
    if csv_file == "quit":
        break
    
    try:
        recipe_book = open(csv_file, 'r+')
        recipe_book.close()
        while True:
            user_input = input("Please select one of the following options:\n  add - Add a new recipe\n  remove - Remove a recipe\n  view - View a recipe\n  calculate - Calculate servings for a recipe\n  quit - Quit the program\n> ")
            if user_input == "quit":
                break
            elif user_input == "add":
                add_recipe(csv_file)
            #elif user_input == "view":
                #view_recipe(recipe_reader)
            print("\n")
        break
    except:
        if csv_file.endswith(".csv"):
            print("Error: That .csv file does not exist, would you like to create a new one? [Y/N] (\"quit\" to quit the program).")
            new_csv = input("> ")
            if new_csv == "quit":
                break
            elif new_csv == "Y":
                create_csv(csv_file)
            elif new_csv == "N":
                pass
            else:
                print("Invalid input\n")
                pass
        else:
            print("Invalid input and/or wrong file type.\n")
            pass


print("[Not sure what to put as the closing text yet]")