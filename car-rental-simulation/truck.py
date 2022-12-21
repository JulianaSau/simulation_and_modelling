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
        self.my_forward(250)

        left(90)
        self.my_forward(120)

        self.my_circle(100, 90, 30)
        
        self.my_setpos(-300, -100)
        
        penup()
        self.my_setpos(-80, -100)
        pendown()
        left(90)
        self.my_forward(105)
        right(-90)
        self.my_forward(10)
        self.my_circle(-72, 183, 30)
        left(90)
        self.my_forward(10)
        right(-90)
        self.my_forward(10)
        
        self.my_circle(-68, 183, 30)
        left(96)
        self.my_forward(15)
        left(90)
        self.my_forward(200)
        left(90)
        self.my_forward(390)
        left(90)
        self.my_forward(190)
        right(90)
        self.my_forward(20)
        left(180)
        self.my_setpos(-80, -100)
        left(-90)
        end_fill()
        
        # door
        penup()
        self.my_setpos(-290, -90)
        pendown()
        left(180)
        self.my_forward(140)
        right(-3)
        self.my_circle(-85, 90, 30)
        right(3)
        self.my_forward(120)
        right(90)
        self.my_forward(230)
        right(90)
        self.my_forward(6)
        right(90)
        self.my_forward(10)
        self.my_circle(68.5, 187, 30)
        right(97)
        self.my_forward(58)
        
        # window
        penup()
        color("Black", "wheat")
        begin_fill()
        self.my_setpos(-280, 30)
        pendown()
        left(-90)
        self.my_forward(20)
        right(-3)
        self.my_circle(-75, 90, 30)
        right(3)
        self.my_forward(110)
        right(90)
        self.my_forward(99)
        right(90)
        self.my_setpos(-280, 30)
        end_fill()
        

        # !st wheel
        penup()
        self.my_setpos(-163, -80)
        self.my_dot(120, "Black")
        pendown()

        # 2nd wheel
        penup()
        self.my_setpos(248, -80)
        self.my_dot(120, "Black")
        pendown()
        
        # 3rd wheel
        penup()
        self.my_setpos(98, -80)
        self.my_dot(120, "Black")
        pendown()
        ht()

    def printTruck(self):
        #Create a Truck object for a used 2002
        #Toyota pickup with 40 000 miles, priced
        #at $12, 000, with a 4-wheel drive.

        print('USED TRUCK INVENTORY')
        print('=====================')

        #Display the truck's data.
        print('The following truck is in inventory:')
        print('Make:', self.get_make())
        print('Model:', self.get_model())
        print('Mileage:', self.get_mileage())
        print('Price:', self.get_price())
        print('Drive type:', self.get_drive_type())
        print()
        self.drawTruck()
