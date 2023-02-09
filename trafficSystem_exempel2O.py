from time import sleep
from statistics import mean, median
from destinations import Destinations
from Lektion_10 import Lane, Vehicle, Light


class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self):
        """Initialize all components of the traffic
        system."""
        self.time = 0
        self.lane_new = Lane(11)
        self.lane_west = Lane(8)
        self.lane_south = Lane(8)
        self.S_after = Lane(3)
        self.W_after = Lane(3)
        self.light_west = Light(14, 6)
        self.light_south = Light(14, 4)
        self.destination = Destinations()
        self.queue = []
        self.queue_blocked = False
        self.stats_S = []
        self.stats_W = []
        self.number_vehicles = 0
        self.X_blocked = 0
        self.cars_in_queue = 0

    def snapshot(self):
        """Print a snap shot of the current state of the system."""
        print(f'{self.W_after} {self.light_west} {self.lane_west}{self.blocked()}{self.lane_new}'
              f'  {str([v.destination for v in self.queue])}\n'
              f'{self.S_after} {self.light_south} {self.lane_south}')

    def step(self):
        """Take one time step for all components."""
        self.step_remove()
        self.move_if_green()
        self.step_lights()
        self.lane_west.step()
        self.lane_south.step()
        self.enter_from_new()
        destination = self.destination.step()
        if len(self.queue) > 0:
            self.cars_in_queue += 1
        if self.lane_new.last_free() is True and len(self.queue) > 0:
            self.lane_new.enter(self.queue.pop(0))
            if destination is not None:
                self.queue.append(Vehicle(destination, self.time))
                self.number_vehicles += 1
        elif self.lane_new.last_free() is True and destination is not None:
            self.lane_new.enter(Vehicle(destination, self.time))
            self.number_vehicles += 1
        elif self.lane_new.last_free() is False and destination is not None:
            self.queue.append(Vehicle(destination, self.time))
            self.number_vehicles += 1
        self.time += 1

    def blocked(self):
        if self.queue_blocked is True:
            return '*'
        else:
            return ' '

    def enter_from_new(self):
        new = self.lane_new.get_first()
        if new is not None:
            if new.destination == 'W' and self.lane_west.last_free() is True:
                self.lane_west.enter(self.lane_new.remove_first())
                self.queue_blocked = False
            elif new.destination == 'S' and self.lane_south.last_free() is True:
                self.lane_south.enter(self.lane_new.remove_first())
                self.queue_blocked = False
            elif new.destination == 'S' or 'W':
                self.queue_blocked = True
                self.X_blocked += 1
        self.lane_new.step()

    def step_remove(self):
        self.W_after.remove_first()
        self.S_after.remove_first()
        self.S_after.step()
        self.W_after.step()

    def move_if_green(self):
        if self.light_west.is_green() is True:
            moved = self.lane_west.remove_first()
            self.W_after.enter(moved)
            if moved is not None:
                self.stats_W.append(self.time - moved.borntime)
        if self.light_south.is_green() is True:
            moved = self.lane_south.remove_first()
            self.S_after.enter(moved)
            if moved is not None:
                self.stats_S.append(self.time - moved.borntime)

    def step_lights(self):
        self.light_west.step()
        self.light_south.step()

    def in_system(self):
        """Return the number of vehicles in the system."""
        lanes = [self.lane_new, self.lane_west, self.lane_south]
        n_cars = len(self.queue)
        for v in lanes:
            n_cars += v.number_in_lane()
        return n_cars

    def print_statistics(self):
        """Print statistics about the run."""
        print(f'Statistics after {self.time} timesteps:\n\n'
              f'Created vehicles:\t {self.number_vehicles}\n'
              f'In system\t:\t  {self.in_system()}\n\n'
              f'At exit\t\t\tWest\t\t\tSouth\n'
              f'Vehicles out:\t\t{len(self.stats_W)}\t\t\t{len(self.stats_S)}\n'
              f'Minimal time:\t\t{min(self.stats_W)}\t\t\t{min(self.stats_S)}\n'
              f'Maximal time:\t\t{max(self.stats_W)}\t\t\t{max(self.stats_S)}\n'
              f'Mean time:\t\t{round(mean(self.stats_W),1)}\t\t\t{round(mean(self.stats_S),1)}\n'
              f'Median time:\t\t{round(median(self.stats_W),1)}\t\t\t{round(median(self.stats_S),1)}\n\n'
              f'Blocked:\t\t{round((self.X_blocked / self.time)*100,1)}%\n'
              f'Queue:\t\t\t{round((self.cars_in_queue / self.time) * 100, 1)}%'
              f'')


def main():
    ts = TrafficSystem()
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0.1)
    print('\nFinal state:')
    ts.snapshot()
    print()
    ts.print_statistics()


if __name__ == '__main__':
    main()
