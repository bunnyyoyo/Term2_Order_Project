import datetime

class Order:
    def __init__(self, selection):
        self.selection = selection
        self.status = 'created'
        now = datetime.datetime.now()
        self.id = int(now.strftime("%Y%m%d%H%M%S"))

    def __repr__(self):
        lines = [
            "=============================",
            "Order #{}".format(self.id),
            "-----------------------------",
            "Order Detail:",
            "-----------------------------",
            self.get_desc(),
            "-----------------------------",
            "{:16s} ${:.2f}".format("Total Price", self.get_price()),
            "============================="
        ]
        return '\n'.join(lines)

    def get_desc(self):
        return '\n'.join(['{:16s} ${:.2f}'.format(record.name, record.price) for record in self.selection])
    def get_price(self):
        return sum([record.price for record in self.selection])


class Record:
    def __init__(self, name, price):
        self.name = name
        self.price = price


noodles = [
    Record('Hokkien noodles', 6), 
    Record('Egg noodles', 6.5), 
    Record('Rice noodles', 5.75),
    Record('Spaghetti', 5),
    Record('Flat noodles', 7)
]
fillings = [
    Record('Chicken', 4), 
    Record('Beef', 4), 
    Record('Fish', 5),
    Record('Tofu', 3.5),
]

sauces = [
    Record('Chilli and basil', 3.5), 
    Record('Oyster and soy', 3), 
    Record('Plum', 2.5),
    Record('Teriyaki', 2.75),
]

#Print the menu 
def pick_menu(food_list, name):
    print ("Pick a {}:".format(name))
    for i, record in enumerate(food_list):
        print("{}: {:16s} ${:.2f}".format(i + 1, record.name, record.price))


    index = -1
    while index == -1:
        try:
            option = int(input("Enter your option: "))
            if option < 1 or option > len(food_list):
                raise Error()
            else:
                index = option - 1
        except:
            print("Wrong Option, Please Enter a Number.")

    return food_list[index]

noodle = pick_menu(noodles, 'noodle')
filling = pick_menu(fillings, 'filling')
sauce = pick_menu(sauces, 'sauce')
selection = [noodle, filling, sauce]
order = Order(selection)

print(order)

order_file = open('orders/test-order-{}.txt'.format(order.id), 'w')
order_file.write(order.__repr__())
