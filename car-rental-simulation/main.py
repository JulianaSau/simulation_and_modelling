from turtle import *
from suv import *
from car import *
from truck import *
import sys
from environment import Environment

WIDTH = 700
HEIGHT = 500

def main():
    try:
        # initalise turtle variables        
        car = Car('BMW', 2001, 70000, 15000.0, 4)
        truck = Truck('Toyota', 2002, 40000, 12000.0, '4WD')
        suv = SUV('Volvo', 2000, 30000, 18500.0, 5)

        main_menu = True
        # put car code here
        while True:
            if main_menu:
                print("""
                    ***** Vehicle Rental Shop *****
                    What would you like to rent?
                    A. Car
                    B. Suv
                    C. Truck
                    Q. Exit
                    """)
                main_menu = False
                choice = input("Enter choice: ")

            if choice != None:
                myWindow = Screen()
                myWindow.setup(WIDTH, HEIGHT)
                myWindow.tracer(False)
                myWindow.bgcolor('wheat')
                env = Environment()
                env.initialiseTurtle()
                env.the_background()
                env.the_sun()
                if choice == "A" or choice == "a":
                    car.printCar()
                elif choice == "B" or choice == "b":
                    suv.printSUV()
                elif choice == "C" or choice == "c":
                    truck.printTruck()
                elif choice == "Q" or choice == "q":
                        exit()
                else:
                    print("Invalid Input. Please Enter A-B-Q")
                    main_menu = True
                env.drawFlowers()
            done()
            myWindow.tracer(True)
            myWindow.exitonclick()
            myWindow.mainloop()
    except:
        if KeyboardInterrupt:
            print()
            print("Thank you for visiting our car rental shop")
        else:   
            exit()


if __name__ == "__main__":
    main()

