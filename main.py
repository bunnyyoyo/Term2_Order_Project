import datetime
import os
import glob
class Order:
    def __init__(self, name, selection):
        self.name = name
        self.selection = selection
        now = datetime.datetime.now()
        self.id = int(now.strftime("%Y%m%d%H%M%S"))

    def __repr__(self):
        lines = [
            "=============================",
            "Order #{} {}".format(self.id, self.name),
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
                raise ValueError()
            else:
                index = option - 1
        except ValueError:
            print("Wrong Option, Please Enter a Number.")

    return food_list[index]

def server_menu():
    name = input("Please Enter Name: ")
    noodle = pick_menu(noodles, 'noodle')
    filling = pick_menu(fillings, 'filling')
    sauce = pick_menu(sauces, 'sauce')
    selection = [noodle, filling, sauce]
    order = Order(name, selection)

    print(order)

    order_file = open('pending-orders/order-{}.txt'.format(order.id), 'w')
    order_file.write(order.__repr__())

def main_menu():
    while True:
        print("========================")
        print("1. Server Menu")
        print("2. Pending Order Menu")
        print("3. Completed Order Menu")
        print("4. Quit")
        try:
            option = int(input("Please Pick an Option: "))
            if option == 1:
                server_menu()
            elif option == 2:
                pending_orders_menu()
            elif option == 3:
                complete_order_menu()
            elif option == 4:
                return True
            else:
                raise ValueError()
            break
        except ValueError:
            print("Option is invalid, Please Enter a valid option")

def pending_orders_menu():
    print("---------------------------")
    print("All pending orders: ")
    files = glob.glob("pending-orders/*.txt")
    for i, filename in enumerate(files):
        order_id = filename[21:-4]
        print("{}. {}". format(i+1, order_id))
    print("Please pick one to view detail or complete")

    index = -1
    while index == -1:
        try:
            option = int(input("Enter order index: "))
            if option < 1 or option > len(files):
                raise ValueError()
            else:
                index = option - 1
        except ValueError:
            print("Invalid Option, Try Again")
    picked_filename = files[index]
    print("Please Choose one option below")
    print("1. View Order Detail")
    print("2. Complete This Order")
    while True:
        try:
            option = int(input("Enter your option: "))
            if option == 1:
                print_order_file(picked_filename)
            elif option == 2:
                new_filepath = picked_filename.replace('pending', 'complete')
                os.rename(picked_filename, new_filepath)
                print("Order-{} has been completed".format(order_id))
            else:
                raise ValueError()
            break
        except ValueError:
            print("Invalid Option, Please Try Again.")

def complete_order_menu():
    print("---------------------------")
    print("All complete orders: ")
    files = glob.glob("complete-orders/*.txt")
    for i, filename in enumerate(files):
        order_id = filename[22:-4]
        print("{}. {}". format(i+1, order_id))
    print("Please pick one to view detail")

    index = -1
    while index == -1:
        try:
            option = int(input("Enter order index: "))
            if option < 1 or option > len(files):
                raise ValueError()
            else:
                index = option - 1
        except ValueError:
            print("Invalid Option, Try Again")
    picked_filename = files[index]
    print_order_file(picked_filename)

def print_order_file(filename):
    file = open(filename)
    for line in file.readlines():
        line = line.strip()
        print(line)

is_terminated = False
while not is_terminated:
    is_terminated = main_menu()