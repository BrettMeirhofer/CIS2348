# Brett Meirhofer 2036955



class ItemToPurchase:
    def __init__(self, name = "none", price = 0, qty=0):
        self.item_name = name
        self.item_price = price
        self.item_quantity = qty

    def print_item_cost(self):
        print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, self.item_price, self.calculate_cost()))

    def calculate_cost(self):
        return self.item_quantity * self.item_price


if __name__ == '__main__':
    Cart = []
    for X in range(0,2):
        print("Item {}".format(X+1))
        Cart.append(ItemToPurchase())
        Cart[-1].item_name = input("Enter the item name:\n")
        Cart[-1].item_price = int(input("Enter the item price:\n"))
        Cart[-1].item_quantity = int(input("Enter the item quantity:\n"))
        if(X < 1):
            print("")

    print("")
    print("TOTAL COST")
    TotalCost = 0
    for Item in Cart:
        Item.print_item_cost()
        TotalCost += Item.calculate_cost()

    print("")
    print("Total: ${}".format(TotalCost))