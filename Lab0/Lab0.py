class Phone:
    def __init__(self):
        self.color = "black"
        self.isOn = False

    def turn_on(self):
        self.isOn = True

    def print_color(self):
        print("Color:", self.color)

    def print_is_on(self):
        if self.isOn:
            print("The phone is on!")
        else:
            print("The phone is off!")