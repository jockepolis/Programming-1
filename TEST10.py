class Destinations:
    """ Generates a sequence of destinations (None, 'W', 'S') """

    def __init__(self):
        """Add internal data."""
        self._arrivals = (  # 0:52, 1:26, 2:22
            2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1,
            2, 1, 1, 0, 2, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 0, 2, 0, 1,
            2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1,
            0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0,
            1, 2, 0, 1, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1)

        self._internal_time = 0
        self._total_cycle = len(self._arrivals)

    def step(self):
        """Make one time step, reporting the destination of the next vehicle
        (or None)."""
        ind = self._arrivals[self._internal_time]
        self._internal_time = (self._internal_time + 1) % len(self._arrivals)
        return 'W' if ind == 1 else 'S' if ind == 2 else None

# Traffic system components


class Vehicle:
    """Represents vehicles in traffic simulations"""

    def __init__(self, destination, borntime):
        """Creates the vehicle with specified properties."""
        # Implement this constructor.


class Lane:
    """Represents a lane with (possibly) vehicles"""

    def __init__(self, length):
        """Creates a lane of specified length."""
        # Implement this constructor.

    def __str__(self):
        """String representation of lane contents."""
        return "a Lane"

    def enter(self, vehicle):
        """Called when a new vehicle enters the end of the lane."""
        # Implement this method.

    def last_free(self):
        """Reports whether there is space for a vehicle at the
        end of the lane."""
        # Implement this method.

    def step(self):
        """Execute one time step."""
        # Implement this method.

    def get_first(self):
        """Return the first vehicle in the lane, or None."""
        # Implement this method.

    def remove_first(self):
        """Remove the first vehicle in the lane.
           Return the vehicle removed.
           If no vehicle is a the front of the lane, returns None
           without removing anything."""
        # Implement this method.

    def number_in_lane(self):
        """Return the number of vehicles currently in the lane."""
        # Implement this method.


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
        # Implement this method.

    def __str__(self):
        """Report current state of the light."""
        return "a Light"

    def step(self):
        """Take one light time step."""
        # Implement this method.

    def is_green(self):
        """Return whether the light is currently green."""
        # Implement this method.


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
