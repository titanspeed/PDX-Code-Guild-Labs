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
        empty_dict = {}
        for i in range(self.spaces):
            empty_dict[i] = None
        return empty_dict

    def make_car(self):
        make = input('What is the make of your car?: ')
        model = input('What is the model of your car?: ')
        year = int(input('What is the year of your car?: '))
        color = input('What is the color of your car?: ')
        car = Vehicle(make, model, year, color)
        return car

    def park(self):
        if self.spaces_left > 0:
            self.make_car()
            self.spaces_left -= 1
            self.parked_vehicles.append(self.make_car())
            print('There are {} spaces left.'.format(self.spaces_left))
        else:
            print('Sorry, parking lot is full.')

    def remove(self):
        car_list = enumerate(self.parked_vehicles)
        for i, v in car_list:
            print('{} is in spot {}'.format(v, i))
        removing = True
        while removing:
            q = input('Which car would you like to remove or (c)ancel? ')
            if q.lower() == 'cancel' or q.lower() == 'c':
                break
            else:
                try:
                    veh = self.parked_vehicles.pop(int(q))
                    self.spaces_left += 1
                    print('{} has left the parking lot.'.format(veh.model))
                    print('There are {} spaces left.'.format(self.spaces_left))
                    removing = False
                except IndexError:
                    print('There is no vehicle in that spot!')
                except ValueError:
                    print('Thats not a valid selection.')

    def program_running(self):
        program_run = True
        while program_run == True:
            decision = input('Would you like to park your (p)ark your car, or (r)emove a car?')
            if decision == 'p' or decision.lower == 'park':
                self.park()
            elif decision.lower == 'r' or decision.lower == 'remove':
                self.remove()

plot = ParkingLot(5)

print(plot.parked_vehicles)

plot.program_running()

# plot.park()

# plot.park(car1)
# plot.park(car2)
# plot.remove()
