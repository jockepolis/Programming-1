# Traffic system components, 2020-11-12

class Vehicle:
    """A simple class representing vehicles in traffic simulations"""

    def __init__(self, destination, borntime):
        self.destination = destination
        self.borntime = borntime

    def __str__(self):
        return f'Vehicle({self.destination}, {self.borntime})'
    
    def get_destination(self):
        return self.destination
    
    def get_borntime(self):
        return self.borntime


class Lane:
    "Represents a lane with (possible) vehicles"

    def __init__(self, length):
        # Initialize all elements to None
        self._the_lane = [None for x in range(length)]

    def __str__(self):
        res = ''
        for s in self._the_lane:
            if s == None:
                res = res + '.'
            else:
                res = res + s.get_destination()
        return '[' + res + ']'

    def enter(self, vehicle):
        if self.last_free():
            self._the_lane[-1] = vehicle
        else:
            raise Exception('Impossible to enter lane: position not free')

    def last_free(self):
        return self._the_lane[-1] == None

    def step(self):
        for i in range(len(self._the_lane)-1):
            if self._the_lane[i] == None:
                self._the_lane[i] = self._the_lane[i+1]
                self._the_lane[i+1] = None

    def get_first(self):
        return self._the_lane[0]

    def remove_first(self):
        v = self._the_lane[0]
        self._the_lane[0] = None
        return v

    def number_in_lane(self):
        return len(self._the_lane) - self._the_lane.count(None)


def demo_lane():
    """For demonstration of the class Lane"""
    a_lane = Lane(10) # space for 10 vehicles
    print(a_lane)
    v = Vehicle('N', 34) # Create a vehicle, borntime 34 and destination N
    a_lane.enter(v) # enter the vehicle in last position of the lane
    print(a_lane)

    a_lane.step() # A time step
    print(a_lane)
    # Simulate 20 time steps
    for t in range(20):
        # every other time step
        if t % 2 == 0:
            u = Vehicle('S', t) # Create a vehicle, borntime t and destination S
            a_lane.enter(u)     # enter the vehicle in last position of the lane
        a_lane.step()           # move the vehicles one step forward in the lane
        print(a_lane)
        # every third time step
        if t % 3 == 0:
            print('  out: ',
                  a_lane.remove_first()) # remove the vehicle in first position
    print('Number in lane:',
          a_lane.number_in_lane())


class Light:
    """Represents a traffic light"""

    def __init__(self, period, green_period):
        self._period = period
        self._green_period = green_period
        self._time = 0

    def __str__(self):
        if self.is_green():
            return '(G)'
        else:
            return '(R)'

    def step(self):
        self._time = (self._time + 1) % self._period

    def is_green(self):
        return self._time < self._green_period


def demo_light():
    """Demonstrats the Light class"""
    a_light = Light(7, 3) # create a light, period 7, green time 3
    # Simulate 15 time steps
    for i in range(15):
        print(i, a_light,
              a_light.is_green())
        a_light.step() # Next step for the light

def main():
    """Demonstrates the classes"""
    print('\nLight demonstration\n')
    demo_light()
    print('\nLane demonstration')
    demo_lane()

if __name__ == '__main__':  # If this file is the main program, you are running:
    main()                  # Call the main function above
    
# When the Python interpreter reads a python file, it defines
# the special variable __name__
# If you are running your module as the main program,
# the interpreter will assign the hard-coded string "__main__" to the __name__ variable
# If this python file is imported by another program, and the your run that program, the
# main function is not called