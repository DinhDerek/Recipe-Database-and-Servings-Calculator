import csv
import os


def remove_recipe(csv_file):
    recipe_name = input("\nEnter the name of the recipe to remove (\"cancel\" to cancel):\n> ")
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
                    print("Recipe successfully removed")
                else:
                    recipe_writer.writerow(recipe)
    os.remove(csv_file)
    os.rename("temp-file.csv", csv_file)
    if recipe_found == False:
        print("That recipe was not found in the .csv file, no recipes were removed")