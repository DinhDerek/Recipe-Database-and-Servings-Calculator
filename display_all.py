'''
Displays all recipes from the .csv file
Example:
(Name).csv
1.Ramen
2.Pho
3.Cheeseburger
'''
import csv
from add_recipe import add_recipe
def display_all(csv_file):
    with open(csv_file) as file:
        recipe_reader = csv.reader(file)
        list_of_dish = [item[0] for item in recipe_reader]
        print(str(len(list_of_dish)) + " recipes found in this file.")
        for index,recipe in enumerate(list_of_dish,1):
            print("  ",index,recipe)


display_all("sample-recipebook.csv")