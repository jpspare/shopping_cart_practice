from IPython.display import clear_output

# Ask the user four bits of input: Do you want to : Show/Add/Delete or Quit?

def shoppingCart():
    """
        Recieves input to either add items to a list (shopping cart), delete items from that list,
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
        if action_check == '1' or action_check == 'show':
            if cart == []:
                print("You cart is currently empty! Let's find you something to purchase!")
            else:
                print("Here is what you have in your cart:")
                for item in cart:
                    print(item)
        
        # Option 2, to add to cart
        elif action_check == '2' or action_check == 'add':
            add_item = input("What would you like to add to your cart? ")
            clear_output()
            add_item_pretty = add_item.title()
            cart.append(add_item.title())
            print("Great! We have added " + add_item + " to your cart!")
            
        # Option 3, to delete from cart
        elif action_check == '3' or action_check == 'delete':
            delete_item = input("What would you like to remove from your cart? ")
            clear_output()
            delete_item_pretty = delete_item.title()
            if delete_item_pretty not in cart:
                print("I'm sorry, you don't have " + delete_item_pretty + " in your cart. Did you want to add that?")
            else:
                cart.remove(delete_item_pretty)
                print("We've removed " + delete_item_pretty + " from your cart!")
                
        # Option 4, to quit and print the cart
        elif action_check == '4' or action_check == 'quit':
            clear_output()
            print('Thank you for shopping at Food and Stuff today! Here is what you purchased:')
            for index, item in enumerate(cart, start=1):
                print(str(index) + ". " + item)
            break
        
        # Alternative if input doesn't match expected values
        else:
            print("I'm sorry, I'm not quite sure what you are looking to do. Please enter one of the following: Show, Add, Delete, or Quit")
            

shoppingCart()