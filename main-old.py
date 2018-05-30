import datetime

class Order:
    def __init__(self, desc, price):
        self.desc = desc
        self.price = price
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
            self.desc,
            "-----------------------------",
            "{:16s} ${:.2f}".format("Total Price", self.price),
            "============================="
        ]
        return '\n'.join(lines)




noodles = [
    ('Hokkien noodles', 6), 
    ('Egg noodles', 6.5), 
    ('Rice noodles', 5.75),
    ('Spaghetti', 5),
    ('Flat noodles', 7)
]
fillings = [
    ('Chicken', 4), 
    ('Beef', 4), 
    ('Fish', 5),
    ('Tofu', 3.5),
]

sauces = [
    ('Chilli and basil', 3.5), 
    ('Oyster and soy', 3), 
    ('Plum', 2.5),
    ('Teriyaki', 2.75),
]

#Print the menu 
def pick_menu(food_list, name):
    print ("Pick a {}:".format(name))
    for (i, (food_type, price)) in enumerate(food_list):
        print("{}: {:16s} ${:.2f}".format(i + 1, food_type, price))


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

    return index

noodle_index = pick_menu(noodles, 'noodle')
filling_index = pick_menu(fillings, 'filling')
sauce_index = pick_menu(sauces, 'sauce')

selection = [noodles[noodle_index], fillings[filling_index],sauces[sauce_index]]

order_dec = '\n'.join(
    ['{:16s} ${:.2f}'.format(food_type, price) for food_type, price in selection]
)
order_price = sum([price for food_type, price in selection])
order = Order(order_dec, order_price)

print(order)
order_file = open('order-{}.txt'.format(order.id), 'w')
order_file.write(order.__repr__())
