from pantry import Pantry
from recipes import Recipes

pantry = Pantry()
recipes = Recipes()

def main():
    while True:
        print("\nPantryPal Menu")
        print("1. Add item")
        print("2. View items")
        print("3. Find meals you can make")
        print("4. Exit")

        choice = input("Enter option: ")

        if choice == "1":
            name = input("Item name: ")
            quantity = input("Quantity: ")
            expiration = input("Expiration date (YYYY-MM-DD): ")
            pantry.add_item(name, quantity, expiration)

        elif choice == "2":
            items = pantry.get_items()
            for item in items:
                print(item)

        elif choice == "3":
            available = [i[1] for i in pantry.get_items()]
            meals = recipes.find_possible_meals(available)
            print("\nMeals you can make:")
            for meal in meals:
                print(meal)

        elif choice == "4":
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()