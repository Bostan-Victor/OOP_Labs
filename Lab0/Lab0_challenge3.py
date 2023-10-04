import math

class Diamond:
    def __init__(self, size):
        self.size = size

    def print_diamond(self):
        stars = 1
        for i in range(math.ceil(self.size/2)):
            for x in range((self.size-stars)//2):
                print(" ", end="")
            for x in range(stars):
                print("*", end="")
            stars += 2
            print()
            
        stars -= 2
        for i in range(round(self.size/2)):
            stars -= 2
            for x in range((self.size-stars)//2):
                print(" ", end="")
            for x in range(stars):
                print("*", end="")
            print()

size = int(input("Enter the size of the diamond: "))

d = Diamond(size)
d.print_diamond()