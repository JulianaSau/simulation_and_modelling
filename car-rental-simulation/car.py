from turtle import *
from vehicle import Automobile

class Car(Automobile):
     #The __init__ method accepts arguments for the
    #car's make, model, price, and doors.
    
    def __init__(self, make, model, mileage, price, doors):
        #Call the superclass's _init__ method and pass 
        #the required arguments. Note that we also have
        #to pass self as an argument.
        Automobile.__init__(self, make, model, mileage, price) 
        
        #Initialize the __doors attribute.
        self.__doors = doors 
        
    #The set_doors method is the mutator for the
    #__doors attribute.
    
    def set_doors(self, doors):
        self.__doors = doors 
        
    #The get_doors method is the accessor for the 
    #__doors attribute.
    
    def get_doors(self):
        return self.__doors 

    def drawCar(self):       
        self.scale = self.random_number_gen()

        if self.x == None:
            self.x = 0
        if self.y == None:
            self.y = 0
        
        # initalise turtle variables
        title("First 3D vehicle with python")
        speed(0)
        bgcolor("wheat")
        pensize(2)
        penup()
        self.my_setpos(-300, -100)
        pendown()
        
        # BODY
        color("Black", self.randvalue)
        begin_fill()
        self.my_setpos(250, -100); 

        left(100)
        forward(90*self.scale)  

        left(30)
        circle(300*self.scale, 45, 30)

        self.my_setpos(-20,80)
        self.my_setpos(-80, 30)
        circle(500*self.scale, 30, 10)
        self.my_setpos(-300, -100)
        end_fill()

        # !st wheel
        penup()
        self.my_setpos(-230, -80)
        dot((self.scale*120), "Black")
        pendown()

        # 2nd wheel
        penup()
        self.my_setpos(170, -80)
        dot((self.scale*120), "Black")
        pendown()
        
        # windows
        penup()
        self.my_setpos(-80, 30)
        pendown()
        self.my_setpos(170, 30)

        # door
        penup()
        self.my_setpos(-80, 30)
        pendown()
        circle(100*self.scale, 88, 10)
        
        penup()
        self.my_setpos(170, 30)
        pendown()
        self.my_setpos(171, -15)
        left(-120)
        circle(80*self.scale, 38, 10)
        left(16)
        circle(80*self.scale, 55, 10)
        left(-12)
        
        penup()
        color("Black","wheat")
        begin_fill()
        self.my_setpos(-70, 30)
        left(120)
        pendown()
        self.my_setpos(-20, 70)
        left(-10)
        forward(55*self.scale)
        left(-20)
        circle(-200*self.scale, 45, 10)
        left(0)
        self.my_setpos(-70, 30)
        end_fill()
        ht()
    
    def printCar(self):
            #Create an SUV object for a used 2000
        #Volvo with 30, 000 miles, priced
        #at $18,500, with 5 passenger capacity.
        car = Car('BMW', 2001, 70000, 15000.0, 4)

        print('USED CAR INVENTORY')
        print('=====================')

        #Display the car's data.
        print('The following car is in inventory:')
        print('Make:', car.get_make())
        print('Model:', car.get_model())
        print('Mileage', car.get_mileage())
        print('Price', car.get_price())
        print('Number of doors:', car.get_doors())
        print()
        car.drawCar()

