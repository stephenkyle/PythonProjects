# This program tests the Car class
import OakfordStephenM09_Ch9_Ex2_CAR

def main():
    # Get the data about the car
    year = input('Enter the model year of the car.')
    make = input('Enter the make of the car.')
    
    # Create an instance of the Car class
    vehicle = OakfordStephenM09_Ch9_Ex2_CAR.Car(year, make)
    for change in range(5):
        vehicle.accelerate()
        speed = vehicle.get_speed()
        print('The new speed is', speed, 'mph.')
    for change in range(5):
        vehicle.brake()
        speed = vehicle.get_speed()
        print('The new speed is', speed, 'mph.')





# Call the main function
main()
