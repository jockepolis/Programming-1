# Traffic system components
from collections import Counter


class Vehicle:
    """Represents vehicles in traffic simulations"""

    def __init__(self, destination, borntime):
        """Creates the vehicle with specified properties."""
        self.destination = destination
        self.borntime = borntime


class Lane:
    """Represents a lane with (possibly) vehicles"""

    def __init__(self, length):
        """Creates a lane of specified length."""
        self.length = length
        self.lane = [None] * length

    def __str__(self):
        """String representation of lane contents."""
        destinations = [c.destination if c is not None else '.' for c in self.lane]
        return f'[{"".join(destinations)}]'

    def enter(self, vehicle):
        """Called when a new vehicle enters the end of the lane."""
        self.lane[-1] = vehicle

    def last_free(self):
        """Reports whether there is space for a vehicle at the
        end of the lane."""
        return True if self.lane[-1] is None else False

    def step(self):
        """Execute one time step."""
        for i in range(1, len(self.lane)):
            if self.lane[i - 1] is None:
                self.lane[i - 1] = self.lane[i]
                self.lane[i] = None

    def get_first(self):
        """Return the first vehicle in the lane, or None."""
        return self.lane[0]

    def remove_first(self):
        """Remove the first vehicle in the lane.
           Return the vehicle removed.
           If no vehicle is a the front of the lane, returns None
           without removing anything."""
        a = self.lane[0]
        self.lane[0] = None
        return a

    def number_in_lane(self):
        """Return the number of vehicles currently in the lane."""
        return len([v for v in self.lane if v is not None])


def demo_lane():
    """For demonstration of the class Lane"""
    a_lane = Lane(10)
    print(a_lane)
    v = Vehicle('N', 34)
    a_lane.enter(v)
    print(a_lane)

    a_lane.step()
    print(a_lane)
    for i in range(20):
        if i % 2 == 0:
            u = Vehicle('S', i)
            a_lane.enter(u)
        a_lane.step()
        print(a_lane)
        if i % 3 == 0:
            print('  out: ',
                  a_lane.remove_first())
    print('Number in lane:',
          a_lane.number_in_lane())


class Light:
    """Represents a traffic light"""

    def __init__(self, period, green_period):
        """Create a light with the specified timers."""
        self.period = period
        self.green_period = green_period
        self.time = 0
        self.green = True

    def __str__(self):
        """Report current state of the light."""
        return '(G)' if self.green is True else '(R)'

    def step(self):
        """Take one light time step."""
        self.time += 1
        if self.time == self.period:
            self.time = 0
            self.green = True

    def is_green(self):
        """Return whether the light is currently green."""
        if self.time >= self.green_period:
            self.green = False
        return self.green


def demo_light():
    """Demonstrats the Light class"""
    a_light = Light(7, 3)
    for i in range(15):
        print(i, a_light,
              a_light.is_green())
        a_light.step()


def main():
    """Demonstrates the classes"""
    print('\nLight demonstration\n')
    demo_light()
    print('\nLane demonstration')
    demo_lane()


if __name__ == '__main__':
    main()
