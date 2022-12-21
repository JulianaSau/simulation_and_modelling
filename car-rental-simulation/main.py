from turtle import *
from suv import *
from car import *
from truck import *
from environment import Environment

WIDTH = 700
HEIGHT = 500

def main():
    try:      
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
                    make = input("Enter car make: ")
                    model = input("Enter car model: ")
                    mileage = input("Enter car mileage: ")
                    price = input("Enter car price: ")
                    doors = input("Enter number of doors : ")
                    if (doors and make and model and price and mileage):
                        car = Car(make, model, mileage, price, doors)
                        car.printCar()
                    else:
                        print("Please enter all fields")
                elif choice == "B" or choice == "b":
                    make = input("Enter suv make: ")
                    model = input("Enter suv model: ")
                    mileage = input("Enter suv mileage: ")
                    price = input("Enter suv price: ")
                    passenger_capacity = input("Enter suv passenger capacity : ")
                    if (mileage and make and model and price and passenger_capacity):
                        suv = SUV(make, model, mileage, price, passenger_capacity)
                        suv.printSUV()
                    else:
                        print("Please enter all fields")
                elif choice == "C" or choice == "c":
                    make = input("Enter truck make: ")
                    model = input("Enter truck model: ")
                    mileage = input("Enter truck mileage: ")
                    price = input("Enter truck price: ")
                    drive_type = input("Enter truck drive type : ")
                    if (mileage and make and model and price and drive_type):
                        truck = Truck(make, model, mileage, price, drive_type)
                        truck.printTruck()
                    else:
                        print("Please enter all fields")
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

