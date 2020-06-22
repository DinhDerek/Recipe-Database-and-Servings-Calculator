import csv
import os

def create_recipe(recipe_name):
    new_recipe = []
    new_recipe.append(recipe_name)
    new_ingredient = input("Enter a new ingredient for " + recipe_name + " (\"done\" to complete the recipe):\n> ")
    while True:
        if new_ingredient == "done" and len(new_recipe) < 3:
            continue_input = input("Warning: no ingredients have been added, enter \"cancel\" to cancel creating this recipe or \"continue\" to add more.\n> ")
            if continue_input == "cancel":
                return 
            elif continue_input == "continue":
                pass
        elif new_ingredient == "done" and len(new_recipe) >= 3:
            break
        else:
            new_recipe.append(new_ingredient)
            new_amount = input("Enter the amount of " + new_ingredient + " in the form of \"amount unit\" Ex.(1 cup)\n> ")
            while float(new_amount.split(" ")[0]) <= 0:
                print("Please enter a positive number.")
                new_amount = input("Enter the amount of " + new_ingredient + " in the form of \"amount unit\" Ex. (1 cup)\n> ")
            new_recipe.append(new_amount)
        new_ingredient = input("Enter a new ingredient for " + recipe_name + " (\"done\" to complete the recipe):\n> ")
    return new_recipe
    

def add_recipe(csv_file):
    recipe_name = input("\nEnter the name of your new recipe to add to the .csv file (\"cancel\" to cancel):\n> ")
    if recipe_name == "cancel":
        return
    else:
        with open(csv_file, 'r+') as read_book, open("temp-file.csv", 'w+', newline='') as write_book:
            recipe_reader = csv.reader(read_book)
            recipe_writer = csv.writer(write_book)
            recipe_found = False
            for recipe in recipe_reader:
                if recipe[0].lower() == recipe_name.lower():
                    recipe_found = True
                    user_input = input("\nThat recipe already exists in the .csv file, would you like to overwrite it? [Y/N] (\"cancel\" to cancel).\n> ")
                    if user_input == "cancel":
                        return 
                    elif user_input == "Y":
                        try:
                            recipe_writer.writerow(create_recipe(recipe_name))
                            print("Recipe added!")
                        except:
                            pass
                    elif user_input == "N":
                        break
                else:
                    recipe_writer.writerow(recipe)
        os.remove(csv_file)
        os.rename("temp-file.csv", csv_file)
        if recipe_found == False:
            with open(csv_file, 'a+') as recipe_book:
                recipe_reader = csv.reader(recipe_book)
                recipe_writer = csv.writer(recipe_book)
                try:
                    recipe_writer.writerow(create_recipe(recipe_name))
                    print("Recipe added!")
                except:
                    return
                return
