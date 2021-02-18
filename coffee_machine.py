class CaffeMachine:
    
    def __init__(self):
        self.intigrients = [400, 540, 120, 9, 550]
        self.type_intigrients = ["water", "milk", "coffee beans", "disposable cups"]
        self.espresso = [-250, 0, -16, -1, 4]
        self.latte = [-350, -75, -20, -1, 7]
        self.cappuccino = [-200, -100, -12, -1, 6]

    def caffe_machine(self):
        print(f"""\nThe coffee machine has:
{self.intigrients[0]} of water
{self.intigrients[1]} of milk
{self.intigrients[2]} of coffee beans
{self.intigrients[3]} of disposable cups
{self.intigrients[4]} of money
""")

    def start_caffe_machine(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):\n")
            if action == "buy":
                caffe = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n ")
                if caffe == "1":
                    self.remaining_intigrients(self.espresso)
                elif caffe == "2":
                    self.remaining_intigrients(self.latte)
                elif caffe == "3":
                    self.remaining_intigrients(self.cappuccino)
                else:
                    continue
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.caffe_machine()
            elif action == "exit":
                break
            else:
                print("Invalid")

    def operation(self, type_of_caffe):
        for i in range(5):
            self.intigrients[i] += type_of_caffe[i]
        return self.intigrients

    def remaining_intigrients(self, type_of_caffe):
        for i in range(5):
            if type_of_caffe[i] + self.intigrients[i] < 0:
                print(f"Sorry, not enough {self.type_intigrients[i]}!")
                return
            else:
                print("I have enough resources, making you a coffee!")
                return self.operation(type_of_caffe)

    def fill(self):
        self.intigrients[0] += int(input("Write how many ml of water do you want to add:\n"))
        self.intigrients[1] += int(input("Write how many ml of milk do you want to add:\n"))
        self.intigrients[2] += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.intigrients[3] += int(input("Write how many disposable cups of coffee do you want to add:\n"))
        return self.intigrients

    def take(self):
        print(f"I gave you ${self.intigrients[4]}")
        self.intigrients[4] = 0


CaffeMachine().start_caffe_machine()
