import csv
from add_recipe import add_recipe
def view_recipe(csv_file):
    with open(csv_file) as file:
        recipe_reader = csv.reader(file)
        all_recipes = [item[0].lower() for item in recipe_reader]
    while True:
        recipe = input("Please enter the name/index of the recipe you want to view:\n> ")
        if recipe.lower() in all_recipes:#makes sure input recipe exists in the .csv
            print(recipe)
            break
        elif recipe.isnumeric(): #check if input consists of numbers or not only
            if 1 <= int(recipe) <= len(all_recipes):
                with open(csv_file) as file:
                    recipe_reader = csv.reader(file)
                    ##make a dictionary storing all the recipes into indexes
                    recipe_dict = dict()
                    for index,recipe_name in enumerate([item[0] for item in recipe_reader],1):
                        recipe_dict[str(index)] = recipe_name
                    #
                    dish_name = recipe_dict[recipe]
                with open(csv_file) as file: #reloops the file reading
                    recipe_reader = csv.reader(file)
                    #grabs list of ingredients given dish name
                    for recipe_name in recipe_reader:
                        recipe_list = [ingredient for ingredient in recipe_name if ingredient != '']
                        if (recipe_list[0].lower() == dish_name.lower()):
                            print(dish_name + ":")
                            ingredients = recipe_list[1::2]
                            measurements = recipe_list[2::2]
                            for i in range(len(ingredients)):
                                print("  " + measurements[i] + " of " + ingredien   ts[i])    
                        #          
            else:
                print("No recipe found at index no.",recipe,"There are only", len(all_recipes),"recipes in this .csv file. Please input a valid index.")
        else:
            print("Error: That recipe does not exist, would you like to create a new one? [Y/N] (\"cancel\" to cancel).")
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

view_recipe("sample-recipebook.csv")