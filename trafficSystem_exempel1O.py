from destinations import Destinations
from Lektion_10 import Lane, Vehicle, Light


class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self):
        """Initialize all components of the traffic
        system."""
        self.time = 0
        self.lane1 = Lane(5)
        self.lane2 = Lane(5)
        self.light = Light(10, 8)
        self.destination = Destinations()
        self.que = []

    def snapshot(self):
        """Print a snap shot of the current state of the system."""
        print(f'{self.lane1} {self.light} {self.lane2}   {str([v.destination for v in self.que])}')

    def step(self):
        """Take one time step for all components."""
        self.lane1.remove_first()
        self.lane1.step()
        if self.light.is_green() is True:
            self.lane1.enter(self.lane2.remove_first())
        self.light.step()
        self.lane2.step()
        destination = self.destination.step()
        if self.lane2.last_free() is True and len(self.que) > 0:
            self.lane2.enter(self.que.pop(0))
            if destination is not None:
                self.que.append(Vehicle(destination, self.time))
        elif self.lane2.last_free() is True and destination is not None:
            self.lane2.enter(Vehicle(destination, self.time))
        elif self.lane2.last_free() is False and destination is not None:
            self.que.append(Vehicle(destination, self.time))
        self.time += 1

    def in_system(self):
        """Return the number of vehicles in the system."""
        pass

    def print_statistics(self):
        """Print statistics about the run."""
        pass


def main():
    ts = TrafficSystem()
    for i in range(34):
        ts.snapshot()
        ts.step()
        # sleep(0.1)
    print('\nFinal state:')
    ts.snapshot()
    print()
    ts.print_statistics()


if __name__ == '__main__':
    main()
