class Vehicle:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.make, self.model, self.year, self.color)

    def __repr__(self):
        return '{} {}'.format(self.color, self.model)


class ParkingLot:
    def __init__(self, spaces):
        self.spaces = spaces
        self.spaces_left = spaces
        self.parked_vehicles = self.create_space_numbers()

    def create_space_numbers(self):
        lot_numbers = {}
        for i in range(1, self.spaces + 1):
            lot_numbers['space_' + str(lot_numbers)] = None
        return lot_numbers

    def list_spaces(self):
        print('++++++++++++++++++++++++++++++++++++++++++')
        for spot_num, veh in self.parked_vehicles.items():
            if veh is None:
                print('{} is available.'.format(spot_num.capitalize()))
            else:
                print('{} {} is parked in {}'.format(veh.color, veh.model, spot_num.capitalize()))

    def make_car(self):
        make = input('What is the make of your car?: ')
        model = input('What is the model of your car?: ')
        year = int(input('What is the year of your car?: '))
        color = input('What is the color of your car?: ')
        car = Vehicle(make, model, year, color)

    return car


def park(self):
    if self.spaces_left > 0:
        car = self.make_car()
        self.list_spaces()
        q = input('Which space number would you like to park this {} {} in?: '.format(car.color, car.model))
        self.parked_vehicles['space_' + q] = car
        self.spaces_left -= 1
        print('{} {} is parked in {}'.format(car.color, car.model, 'space_' + q.capitalize()))
    else:
        print('There are no spaces left.')


def retrieve(self):
    self.list_spaces()
    q = input('Which space number would you like to retrieve?: ')
    if int(q) in range(1, self.spaces + 1) and self.parked_vehicles['space_' + q] is not None:
        self.parked_vehicles['space_' + q] = None
        self.spaces_left += 1
    else:
        print('There is no vehicle in that spot.')


def main_interface(self):
    while True:
        q = input('Would you like to (P)ark, (R)etrieve, (L)ist Spaces or (Q)uit?: ')
        if q.lower() == 'p':
            self.park()
        elif q.lower() == 'r':
            self.retrieve()
        elif q.lower() == 'l':
            self.list_spaces()
        elif q.lower() == 'q':
            print('Goodbye.')
            quit()
        else:
            print('I did not understand that. Please try again.')


plot = ParkingLot(5)
plot.main_interface()
# plot.park(car1)
# plot.park(car2)
# plot.remove()
