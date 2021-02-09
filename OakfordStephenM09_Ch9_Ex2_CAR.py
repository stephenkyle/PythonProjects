# The Car class holds data about the car.
class Car:
    # The init method initializes the attributes 
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    # Accelerate method adds 5 to the speed data
    def accelerate(self):
        self.__speed += 5

    # Brake method subtracts 5 from the speed data
    def brake(self):
        self.__speed -=5

    # Get_speed method returns the current speed
    def get_speed(self):
        return self.__speed

# Stephen Oakford
