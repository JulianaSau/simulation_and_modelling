from turtle import *
from vehicle import Automobile

class Truck(Automobile):
    #The __init__ method accepts arguments for the
    #Truck's make, model, mileage, price, and drive type.

    def __init__(self, make, model, mileage, price, drive_type):
        #Call the superclass's __init__ method and pass
        #the required arguments. Note that we also have
        #to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)

        #Initialize the drive_type attribute.
        self.__drive_type = drive_type

    #The set_drive_type method is the mutator for the
    #__drive_type attribute.

    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type

    #The get_drive_type  method is the accessor for the
    #__drive_type attribute.

    def get_drive_type(self):
        return self.__drive_type
    
    def drawTruck(self):
        self.scale = self.random_number_gen()

        if self.x == None:
            self.x = 0
        if self.y == None:
            self.y = 0

        # initialise starting posistion
        penup()
        self.my_setpos(-300, -100)
        pendown()

        # BODY
        color("Black", self.randvalue)
        begin_fill()
        self.my_setpos(-80, -100)

        left(90)
        forward(250*self.scale)

        left(90)
        forward(120*self.scale)

        circle(100*self.scale, 90, 30)
        
        self.my_setpos(-300, -100)
        
        penup()
        self.my_setpos(-80, -100)
        pendown()
        left(90)
        forward(105*self.scale)
        right(-90)
        forward(10*self.scale)
        circle(-72*self.scale, 183, 30)
        left(90)
        forward(10*self.scale)
        right(-90)
        forward(10*self.scale)
        # # forward(380*self.scale)
        circle(-68*self.scale, 183, 30)
        left(96)
        forward(15*self.scale)
        left(90)
        forward(200*self.scale)
        left(90)
        forward(390*self.scale)
        left(90)
        forward(190*self.scale)
        right(90)
        forward(20*self.scale)
        left(180)
        self.my_setpos(-80, -100)
        left(-90)
        end_fill()
        
        # door
        penup()
        self.my_setpos(-290, -90)
        pendown()
        left(180)
        forward(140*self.scale)
        right(-3)
        circle(-85*self.scale, 90, 30)
        right(3)
        forward(120*self.scale)
        right(90)
        forward(230*self.scale)
        right(90)
        forward(6*self.scale)
        right(90)
        forward(10*self.scale)
        circle(68.5*self.scale, 187, 30)
        right(97)
        forward(58*self.scale)
        
        # window
        penup()
        color("Black", "wheat")
        begin_fill()
        self.my_setpos(-280, 30)
        pendown()
        left(-90)
        forward(20*self.scale)
        right(-3)
        circle(-75*self.scale, 90, 30)
        right(3)
        forward(110*self.scale)
        right(90)
        forward(99*self.scale)
        right(90)
        self.my_setpos(-280, 30)
        end_fill()
        

        # !st wheel
        penup()
        self.my_setpos(-163, -80)
        dot((self.scale*120), "Black")
        pendown()

        # 2nd wheel
        penup()
        self.my_setpos(248, -80)
        dot((self.scale*120), "Black")
        pendown()
        
        # 3rd wheel
        penup()
        self.my_setpos(98, -80)
        dot((self.scale*120), "Black")
        pendown()
        ht()

    def printTruck(self):
        #Create a Truck object for a used 2002
        #Toyota pickup with 40 000 miles, priced
        #at $12, 000, with a 4-wheel drive.
        truck = Truck('Isuzu', 2002, 40000, 12000.0, '4WD')

        print('USED TRUCK INVENTORY')
        print('=====================')

        #Display the truck's data.
        print('The following truck is in inventory:')
        print('Make:', truck.get_make())
        print('Model:', truck.get_model())
        print('Mileage:', truck.get_mileage())
        print('Price:', truck.get_price())
        print('Drive type:', truck.get_drive_type())
        print()
        truck.drawTruck()
