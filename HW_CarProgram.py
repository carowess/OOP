
import HW_CarClass as c

def main():

    car1 = c.Car('Toyota', 'Camry')

    print()

    for x in range(5):
        car1.accelerate()
        print('The current speed is:',car1.get_speed(),'mph.')

    for x in range(5):
        car1.brake()
        print ('The current speed is:',car1.get_speed(),'mph.')

    print()
    
main()