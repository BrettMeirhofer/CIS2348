# Brett Meirhofer 2036955



class ItemToPurchase:
    def __init__(self, name = "none", price = 0, qty = 0, description = "none"):
        self.item_name = name
        self.item_description = description
        self.item_price = price
        self.item_quantity = qty

    def print_item_cost(self):
        print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, self.item_price, self.calculate_cost()))

    def calculate_cost(self):
        return self.item_quantity * self.item_price


class ShoppingCart:
    def __init__(self, name= "none", date="January 1, 2016", items = []):
        self.customer_name = name
        self.current_date = date
        self.cart_items = items

    def add_item(self, item):
        self.cart_items.append(item)
        print("")

    def remove_item(self, item_name):
        for CurrentItem in self.cart_items:
            if CurrentItem.item_name == item_name:
                self.cart_items.remove(CurrentItem)
                break
        else:
            print("Item not found in cart. Nothing removed.")

        print("")


    def modify_item(self, ItemToPurchase):
        for CurrentItem in self.cart_items:
            if CurrentItem.item_name == ItemToPurchase.item_name:
                CurrentItem.item_quantity = ItemToPurchase.item_quantity
                break
        else:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = 0
        for CurrentItem in self.cart_items:
            num_items += CurrentItem.item_quantity

        return num_items

    def get_cost_of_cart(self):
        cart_cost = 0
        for CurrentItem in self.cart_items:
            cart_cost += CurrentItem.calculate_cost()

        return cart_cost

    def print_total(self):
        print("OUTPUT SHOPPING CART")
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date))
        print("Number of Items: {}".format(self.get_num_items_in_cart()))
        print("")
        if len(self.cart_items) > 0:
            for CurrentItem in self.cart_items:
                CurrentItem.print_item_cost()
        else:
            print("SHOPPING CART IS EMPTY")

        print("")
        print("Total: ${}".format(self.get_cost_of_cart()))
        print("")


    def print_descriptions(self):
        print("OUTPUT ITEMS' DESCRIPTIONS")
        print("{}'s Shopping Cart - {}".format(self.customer_name,self.current_date))
        print("")
        print("Item Descriptions")
        for CurrentItem in self.cart_items:
            print("{}: {}".format(CurrentItem.item_name,CurrentItem.item_description))
        print("")


def PrintMenu():
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print("")
    while True:
        print("Choose an option:")
        UserInput = input()

        if UserInput == "a":
            print("ADD ITEM TO CART")
            CurrentItem = ItemToPurchase()
            CurrentItem.item_name = input("Enter the item name:\n")
            CurrentItem.item_description = input("Enter the item description:\n")
            CurrentItem.item_price = int(input("Enter the item price:\n"))
            CurrentItem.item_quantity = int(input("Enter the item quantity:\n"))
            CurrentCart.add_item(CurrentItem)
            PrintMenu()
            break

        if (UserInput == "r"):
            print("REMOVE ITEM FROM CART")
            CurrentCart.remove_item(input("Enter name of item to remove:\n"))
            PrintMenu()
            break

        if(UserInput == "c"):
            print("CHANGE ITEM QUANTITY")
            CurrentItem = ItemToPurchase()
            CurrentItem.item_name = input("Enter the item name:\n")
            CurrentItem.item_quantity = int(input("Enter the new quantity:\n"))
            CurrentCart.modify_item(CurrentItem)
            print("")
            PrintMenu()
            break

        if (UserInput == "i"):
            CurrentCart.print_descriptions()
            PrintMenu()
            break

        if (UserInput == "o"):
            CurrentCart.print_total()
            PrintMenu()
            break


        if UserInput == "q":
            break



if __name__ == '__main__':
    CurrentCart = ShoppingCart()
    CurrentCart.customer_name = input("Enter customer's name:\n")
    CurrentCart.current_date = input("Enter today's date:\n")
    print("")
    print("Customer name: {}".format(CurrentCart.customer_name))
    print("Today's date: {}".format(CurrentCart.current_date))
    print("")
    PrintMenu()









