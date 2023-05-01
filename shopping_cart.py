from IPython.display import clear_output

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

def shopping_cart():
    """
    Receives input to either add items to a list (shopping cart), delete items from that list,
    view the list, or tell the function to quit, at which any items in the cart will be printed
    for viewing.
    """

    cart = []

    shopping = True

    while shopping:
        # Intro message and input
        print("\nWelcome to Food and Stuff! What would you like to do today?")
        action = input("\n1. Show my cart \n2. Add to my cart \n3. Delete something from my cart \n4. Quit\n")
        clear_output()
        action_check = action.lower()

        # Option 1, to view cart
        if action_check in ['1', 'show']:
            if not cart:
                print("You cart is currently empty! Let's find you something to purchase!")
            else:
                print("Here is what you have in your cart:")
                for item in cart:
                    print(item)

        # Option 2, to add to cart
        elif action_check in ['2', 'add']:
            add_item = input("What would you like to add to your cart? ")
            clear_output()
            add_item_pretty = add_item.title()
            cart.append(add_item.title())
            print(f"Great! We have added {add_item} to your cart!")

        # Option 3, to delete from cart
        elif action_check in ['3', 'delete']:
            delete_item = input("What would you like to remove from your cart? ")
            clear_output()
            delete_item_pretty = delete_item.title()
            if delete_item_pretty not in cart:
                print(f"I'm sorry, you don't have {delete_item_pretty} in your cart. Did you want to add that?")
                add_delete = input("Did you want to add that? Yes/No ")
                add_delete_check = add_delete.title()
                clear_output()
                if add_delete_check == 'Yes':
                    cart.append(delete_item_pretty)
                    print(f"Great! We have added {delete_item_pretty} to your cart!")
                elif add_delete_check == 'No':
                    print("Not a worry, we won't add that!")
            else:
                clear_output()
                cart.remove(delete_item_pretty)
                print(f"We've removed {delete_item_pretty} from your cart!")

        # Option 4, to quit and print the cart
        elif action_check in ['4', 'quit']:
            clear_output()
            print('Thank you for shopping at Food and Stuff today! Here is what you purchased:')
            for index, item in enumerate(cart, start=1):
                print(f"{index}. {item}")
            break

        # Alternative if input doesn't match expected values
        else:
            print("I'm sorry, I'm not quite sure what you are looking to do. Please enter one of the following: Show, Add, Delete, or Quit")


shopping_cart()
