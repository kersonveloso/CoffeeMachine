class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.ok = True
        self.coffee_ = []
        self.resources = [
            [250, 0, 16, 1, 4],  # espresso
            [350, 75, 20, 1, 7],  # latte
            [200, 100, 12, 1, 6]  # cappuccino
        ]
        self.active = True
        self.action = ''
        self.buy = 0

    def show(self):
        print(f"The coffee machine has: ")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def take(self):
        print(f"I gave you ${self.money}\n")
        self.money = 0

    def coffee(self):
        if self.water < self.coffee_[0]:
            print("Sorry, not enough coffee!")
            self.ok = False
        elif self.milk < self.coffee_[1]:
            print("Sorry, not enough milk!")
            self.ok = False
        elif self.beans < self.coffee_[2]:
            print("Sorry, not enough beans!")
            self.ok = False
        elif self.cups < self.coffee_[3]:
            print("Sorry, not enough cups!")
            self.ok = False
        else:
            self.ok = True

    def make_coffee(self):
        self.buy = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if self.buy == '1' or self.buy == '2' or self.buy == '3':
            self.buy = int(self.buy)
            self.coffee_ = self.resources[self.buy-1]
            self.coffee()
            if self.ok:
                self.water -= self.coffee_[0]
                self.milk -= self.coffee_[1]
                self.beans -= self.coffee_[2]
                self.cups -= self.coffee_[3]
                self.money += self.coffee_[4]

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do want to add:\n"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
        print()

    def menu(self):
        while self.active:
            self.action = input("Write action (buy, fill, take, remaining, exit):\n")
            print()
            if self.action == 'buy':
                self.make_coffee()
            elif self.action == 'fill':
                self.fill()
            elif self.action == 'take':
                self.take()
            elif self.action == 'remaining':
                self.show()
            else:
                self.active = False


cm = CoffeeMachine(400, 540, 120, 9, 550)
cm.menu()
