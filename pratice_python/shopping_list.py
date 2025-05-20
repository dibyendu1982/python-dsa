# Create a shopping list and add/remove items.

shopping_list = []

def add_item(item):
    shopping_list.append(item)
    print(f"{item} has been added to the shopping list.")
    
def remove_item(item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the shopping list.")
    else:
        print(f"{item} is not in the shopping list.")

def view_list():
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("Shopping list:")
        for item in shopping_list:
            print(f"- {item}")

def main():
    while True:
        print("\nShopping List Application")
        print("1. Add item")