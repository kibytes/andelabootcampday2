class  Car:
    def __init__(self, color):
        self.price = 15000
        self.color = color
 
    def set_price(self, price1):
        self.price = price1
        print "Car price is:" + str(self.price) + "Kenyan shillings"
 
    def set_color(self, color):
        self.color = color

    def get_color(self):
        print "The color of the car is:" + self.color
 
class Bus(Car):
    def __init__(self, color, seats):
        Car.__init__(self, color)
        self.seats = seats

    def set_color(self, color, aprint):
        self.color = color + " " + aprint
    
    def get_passengers_num(self):
        #passengers = num of seats minus driver and conductor seats
        print "Bus can accomodate " + str(self.seats - 2) + " people"

class Truck(Car):
    def __init__(self, weight):
        Car.__init__(self, "Yellow")
        self.weight = weight

    def get_weight(self):
        print "The truck weighs " + str(self.weight) + " kilograms"

    def load(self, wt):
        print "Loading items into truck....."
        self.weight = self.weight + wt

    def mustBeWeighedAtBridge(self):
        if self.weight > 10000:
            print "Truck must go through the weigh bridge"
        else:
            print "Truck may move along without passing through weigh bridge"

##atruck = Truck(8000)
##atruck.get_weight()
##atruck.load(5000)
##atruck.get_weight()
##atruck.mustBeWeighedAtBridge()
