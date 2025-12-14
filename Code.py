#Small Recipe Management
from abc import ABC , abstractmethod
class Recipe(ABC):
    def __init__ (self,name,ingredients,instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

    @abstractmethod
    def display_recipe(self):
            pass
#child class 1 : veg recipe (polymorphism)
class VegRecipe(Recipe):
    def display_recipe(self):
        print("\n---VEG RECIPE---")
        print(f"Name : {self.name}")
        print("Ingredients :",",".join(self.ingredients))
        print(f"Instructions : {self.instructions}")
#child class 2: Non-veg recipe(polymorphism)

class NonVegRecipe(Recipe):
    def display_recipe(self):
        print("\n---NON VEG RECIPE---")
        print(f"Name : {self.name}")
        print("Ingredients :",",".join(self.ingredients))
        print(f"Instructions : {self.instructions}")

#Recipe Manager : Handles Collection (Encapsulation)

class RecipeManager:
    def __init__(self):
        self.recipes=[] #encapsulated list

    def add_recipe(self,recipe):
        self.recipes.append(recipe)
        print("Recipe Added Successfully")

    def show_all_recipe(self):
        if not self.recipes:
            print("No recipes available")
        else:
            for recipe in self.recipes:
                recipe.display_recipe()
    def search_by_name(self,name):
        found = False
        for recipe in self.recipes:
            if recipe.name.lower()==name.lower():
                recipe.display_recipe()
                found = True
                break
        if not found:
            print("Recipe not found")
            
       
#Main program - Interface for user

def main():

    manager = RecipeManager()

    while True:
        print("\n--------Recipe Management System---------")
        print("1. Add Recipe")
        print("2. Show all recipe")
        print("3. Search Recipe by name")
        print("4.Exit")

        choice = int(input("Enter your Choice here: "))

        if choice == 1: #choice 1

            name = input("Enter Recipe name: ")
            is_veg = input("Is is Veg?(Yes/No): ").strip().lower()
            ingredients = input("Enter ingredients (Comma-separate): ").split(",")
            instructions = input("Enter Instructions : ")

            if is_veg == 'yes':
                recipe = VegRecipe(name,ingredients,instructions)
            else:
                 recipe = NonVegRecipe(name,ingredients,instructions)
            manager.add_recipe(recipe)
                 
        elif choice == 2: #choice 2
            manager.show_all_recipe()
            
        elif choice == 3: #choice 3
            search_name = input("Enter the recipe name to search: ")
            manager.search_by_name(search_name)

        elif choice == 4 : #choice 4
            print("Exiting.... Thank You")
            break
        else :
             print("Invalid choice . Try again")
             
 
        
#Run the program

if __name__ == "__main__":
    main()
