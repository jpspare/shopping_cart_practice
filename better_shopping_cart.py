class ShoppingCart():
    """
        The ShoppingCart class has methods for adding items to a list
        (shopping cart), deleting items from that list, and viewing the
        list.

        Attibute for class:
        - Cart: expected to be an empty list
    """

    def __init__(self, cart):
        self.cart = cart

    #'while' method to continue program running until user quits
    # Also ensures that input argument is an empty list
    def run(self):
        if self.cart != []:
            print(f"All items in your cart have been returned to your car. You cart is now empty.")
            self.cart = []
        while self.run1():
            pass

    # Method for running the program, getting user input to determine which
    # subsequent methods to use
    def run1(self):
        possible_actions = [
            {'name': 'show', 'fn': self.showCart},
            {'name': 'add', 'fn': self.addCart},
            {'name': 'delete', 'fn': self.deleteCart},
            {'name': 'quit', 'fn': self.quitCart},
        ]
        
        print("\nWelcome to Food and Stuff! What would you like to do today?")
        action_input = input("\n1. Show my cart \n2. Add to my cart \n3. Delete something from my cart \n4. Quit\n")
        action = None

        try:
            i = int(action_input)
            if i >= 1 and i <= len(possible_actions):
                action = possible_actions[i-1]
                return action['fn']()
        except ValueError:
            pass
        if not action:
            for option in possible_actions:
                if option['name'].lower().startswith(action_input.lower()):
                    action = option
                    return action['fn']()
        if not action:
            print(f"I'm sorry, I'm not sure what '{action_input}' means. Please enter one of the following: Show, Add, Delete, or Quit")
            return self.run1
        else: #Fail catch in case 'ifs' don't cover all input options
            print("Whoops, shouldn't be able to get here!")


    # Method for viewing the cart
    def showCart(self):
        if self.cart == []:
            print("You cart is currently empty! Let's find you something to purchase!")
        else:
            print("Here is what you have in your cart:")
            for item in self.cart:
                print(item)
        return self.run1
    

    # Method for adding to the cart
    def addCart(self):
        item_to_add = input("What would you like to buy today? ")
        self.cart.append(item_to_add.title())
        print(f'Great! We have added {item_to_add.title()} to your cart!')
        return self.run1


    # Method for deleting from cart
    def deleteCart(self):
        item_to_delete = input("what would you like to remove from your cart? ")
        if item_to_delete.title() not in self.cart:
            print(f"I'm sorry, you don't have {item_to_delete.title()} in your cart. Did you want to add that?")
            add_delete = input("Did you want to add that Yes/No ")
            add_delete_check = add_delete.title()
            if add_delete_check == 'Yes':
                self.cart.append(item_to_delete.title())
                print(f"Great! We have added {item_to_delete.title()} to your cart!")
                return self.run1
            elif add_delete_check == 'No':
                print("Not a worry, we won't add that!")
                return self.run1
        else:
            self.cart.remove(item_to_delete.title())
            print(f"We've removed {item_to_delete.title()} from your cart!")
            return self.run1


    # Method for quitting the program and printing the items in the cart
    def quitCart(self):
        if self.cart == []:
            print('\nThank you for coming in today. Perhaps you will find something to purchase next time!')
        else:
            print('\nThank you for shopping at Food and Stuff today! Here is what you purchased:')
            for index, item in enumerate(self.cart, start=1):
                print(str(index) + ". " + item)
        return False


if __name__ == "__main__":
    ShoppingCart([]).run()