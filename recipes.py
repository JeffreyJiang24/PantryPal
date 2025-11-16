class Recipes:
    def __init__(self):
        self.recipe_book = {
            "Pasta": ["pasta", "salt"],
            "Fried Rice": ["rice", "egg", "soy sauce"],
            "Sandwich": ["bread", "cheese"],
        }

    def find_possible_meals(self, available_items):
        available_lower = [i.lower() for i in available_items]

        possible = []
        for meal, ingredients in self.recipe_book.items():
            if all(ingredient in available_lower for ingredient in ingredients):
                possible.append(meal)

        return possible