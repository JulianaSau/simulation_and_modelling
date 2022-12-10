from turtle import *
from vehicle import Automobile

class SUV(Automobile):
    #The __init__ method accepts arguments for the
    #car's make, model, price, and doors.
    
    def __init__(self, make, model, mileage, price, pass_cap):
        # Call the superclass's _init__ method and pass
        # the required arguments. Note that we also have
        # to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price)
        #Initialize the __pass_cap attribute.
        self.__pass_cap = pass_cap

    #The set_pass_cap method is the mutator for the
    #__pass_cap attribute.

    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap

    #The get_pass_cap method is the accessor for the
    # __pass_cap attribute.

    def get_pass_cap(self):
        return self.__pass_cap
    
    def drawSuv(self):
        
        self.scale = self.random_number_gen()

        if self.x == None:
            self.x = 0
        if self.y == None:
            self.y = 0
        
        # initialise starting posistion
        penup()
        self.my_setpos(-250, -100)
        pendown()

        # BODY
        color("Black", self.randvalue)
        begin_fill()
        self.my_setpos(330, -100)

        left(92)
        forward(100*self.scale)  
        
        left(30)
        circle(400*self.scale, 20, 30)

        self.my_setpos(239, 100)
        self.my_setpos(0, 100)
        self.my_setpos(-80, 30)
        self.my_setpos(-200, 30)
        left(90)
        circle(400*self.scale, 15, 30)
        self.my_setpos(-250, -100)
        left(-105)
        end_fill()

        # !st wheel
        penup()
        self.my_setpos(-100, -80)
        dot((self.scale*120), "Black")
        pendown()

        # 2nd wheel
        penup()
        self.my_setpos(240, -80)
        dot((self.scale*120), "Black")
        pendown()
        
        # windows
        penup()
        color("Black", "wheat")
        begin_fill()
        self.my_setpos(-60, 30)
        pendown()
        self.my_setpos(285, 30)
        right(50)
        forward(10*self.scale)
        left(40)
        circle(400*self.scale, 10, 30)
        left(38)
        forward(230*self.scale)
        left(20)
        self.my_setpos(-60, 30)
        end_fill()
        
        # door
        penup()
        self.my_setpos(90, 88)
        pendown()
        self.my_setpos(90, -90)
        penup()
        # first door
        self.my_setpos(-60, 30)
        pendown()

        left(70)
        forward(55*self.scale)
        left(70)
        circle(-46*self.scale, 100, 30)
        left(120)
        forward(204*self.scale)
        left(90)
        circle(-80*self.scale, 81, 30)
        left(81.04)
        forward(100*self.scale)
        
        ht()


    def printSUV(self):
        #Create an SUV object for a used 2000
        #Volvo with 30, 000 miles, priced
        #at $18,500, with 5 passenger capacity.
        suv = SUV('Volvo', 2000, 30000, 18500.0, 5)

        print('USED SUV INVENTORY')
        print('=====================')

        #Display the SUV's data
        print('The following SUV is in inventory.')
        print('Make:', suv.get_make())
        print('Model:', suv.get_model())
        print('Mileage:', suv.get_mileage())
        print('Price', suv.get_price())
        print('Passenger Capacity:', suv.get_pass_cap())
        suv.drawSuv()








