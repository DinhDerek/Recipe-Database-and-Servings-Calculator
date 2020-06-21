import csv

def create_csv(csv_file):
    while True:
        try:
            new_csv = open(csv_file, mode='w+')
            new_csv.close()
            print("New .csv file successfully created.")
            break
        except:
            print("Invalid character found in the file name, please try again.\n")
            pass


def view_recipe(recipe_reader):
    recipe_name = input("Please enter the name of the recipe:\n> ")
    print(recipe_name)

print("[Not sure what to put as the welcome text yet]")
while True:
    print("Please enter a .csv file to begin (\"quit\" to quit the program).")
    csv_file = input("> ")
    if csv_file == "quit":
        break
    
    try:
        with open(csv_file, newline='') as recipe_book:
            recipe_reader = csv.reader(recipe_book)
            for recipe in recipe_reader:
                recipe = [ingredient for ingredient in recipe if ingredient != '']
                #print(recipe)
            while True:
                print("Please select one of the following options:\n  add - Add a new recipe\n  remove - Remove a recipe\n  view - View a recipe\n  calculate - Calculate servings for a recipe\n  quit - Quit the program\n  ")
                user_input = input("> ")
                if user_input == "quit":
                    break
                elif user_input == "view":
                    view_recipe(recipe_reader)
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



'''
while user_input != "quit":
    if user_input == "add":
    elif user_input == "remove":
    elif user_input == "view":
    elif 
    pass
'''
print("[Not sure what to put as the closing text yet]")