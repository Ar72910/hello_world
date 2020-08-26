class Coffee:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.cash = 550

    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        types_of_coffee = input()

        if types_of_coffee == "1":
            if self.water >= 250 and self.milk >= 0 and self.beans >= 16 and self.cups >= 1:
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.cash += 4
                print("I have enough resources, making you a coffee!")
            else:
                if self.water < 250:
                    print("Sorry, not enough water!")
                elif self.beans < 16:
                    print("Sorry, not enough beans!")
                elif self.cups < 1:
                    print("Sorry, not enough cups!")

        if types_of_coffee == "2":
            if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.cash += 7
            else:
                if self.water < 350:
                    print("Sorry, not enough water!")
                elif self.beans < 20:
                    print("Sorry, not enough beans!")
                elif self.cups < 1:
                    print("Sorry, not enough cups!")
                elif self.milk < 75:
                    print("Sorry, not enough milk!")

        if types_of_coffee == "3":
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.cash += 6

            else:
                if self.water < 200:
                    print("Sorry, not enough water!")
                elif self.beans < 12:
                    print("Sorry, not enough beans!")
                elif self.cups < 1:
                    print("Sorry, not enough cups!")
                elif self.milk < 100:
                    print("Sorry, not enough milk!")

        else:
            return


    def fill(self):
        w=int(input('Write how many ml of water do you want to add:\n '))
        m=int(input('Write how many ml of milk do you want to add:\n '))
        b=int(input('Write how many grams of coffee beans do you want to add:\n '))
        cp=int(input('Write how many disposable cups of coffee do you want to add:\n '))
        self.water += w
        self.milk += m
        self.beans += b
        self.cups += cp

    def take(self):
        print("I gave you $", self.cash, sep="")
        self.cash = 0

    def rem(self):
        print("The coffee machine has:")
        print(self.water, "of water")
        print(self.milk, "of milk")
        print(self.beans, "of coffee beans")
        print(self.cups, "of disposable cups")
        print("$" + str(self.cash), "of money")

    def action(self):
        while True:
            print('Write action (buy, fill, take, remaining, exit):')
            act = input()
            if act == 'buy':
                self.buy()
            elif act == 'fill':
                self.fill()
            elif act == 'take':
                self.take()
            elif act == 'remaining':
                self.rem()
            elif act == 'exit':
                break
ac = Coffee()
ac.action()
