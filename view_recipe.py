import csv
from add_recipe import add_recipe
def view_recipe(csv_file):
    with open(csv_file) as file:
        recipe_reader = csv.reader(file)
        all_recipes = [item[0].lower() for item in recipe_reader]
    while True:
        recipe = input("Please enter the name of the recipe you want to view:\n> ")
        if recipe.lower() in all_recipes:
            break
        else:
            print("Error: That recipe does not exist, would you like to create it? [Y/N] (\"cancel\" to cancel).")
            recipe_input = input("> ")
            if recipe_input == "cancel":
                return
            elif recipe_input == "Y":
                add_recipe(csv_file)
                return
            elif recipe_input == "N":
                pass
            else:
                print("Invalid input\n")
                pass
    with open(csv_file) as file:
        recipe_reader = csv.reader(file)
        for recipe_name in recipe_reader:
            recipe_list = [ingredient for ingredient in recipe_name if ingredient != '']
            if (recipe_list[0].lower() == recipe.lower()):
                print(recipe + ":")
                ingredients = recipe_list[1::2]
                measurements = recipe_list[2::2]
                for i in range(len(ingredients)):
                    print("  " + measurements[i] + " of " + ingredients[i])
