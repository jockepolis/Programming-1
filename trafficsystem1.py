from destinations import Destinations
from trafficsystemcomponents import Light, Lane, Vehicle
from time import sleep


class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self):
        self.time = 0
        self.lane1 = Lane(5)
        self.lane2 = Lane(5)
        self.light = Light(10, 6)
        self.destination = Destinations()
        self.queue = []

    def snapshot(self):
        """Prints a snapshot of the current state of the system"""
        print(f'{self.lane1} {self.light} {self.lane2}   {str([v.destination for v in self.queue])}')

    def step(self):
        """Takes one step for all components in the system"""
        self.lane1.remove_first()
        self.lane1.step()
        if self.light.is_green() is True:
            self.lane1.enter(self.lane2.remove_first())        #om det är grönt, gå in i lane1 och ur lane2
        self.light.step()
        self.lane2.step()
        destination = self.destination.step()                 #anropar step-metoden i destinations
        if self.lane2.last_free() is True and len(self.queue) > 0:  #om sista platsen i lane2 är ledig och det finns någon i kön
            self.lane2.enter(self.queue.pop(0))                 #gå in i lane2 och ta bort från kön
            if destination is not None:                          #om destination returnerar en destination
                self.queue.append(Vehicle(destination, self.time))      #lägg till en bil i kön
        elif self.lane2.last_free() is True and destination is not None:     #om sista platsen i lane2 är ledig och destination returnerar en destination
            self.lane2.enter(Vehicle(destination, self.time))            #lägg till bilen i lane2
        elif self.lane2.last_free() is False and destination is not None:  #om sista platsen i lane2 är upptagen och destination returnerar en destination
            self.queue.append(Vehicle(destination, self.time))      #lägg bilen sist i kön
        self.time += 1

    def in_system(self):
        pass  # do nothing

    def print_statistics(self):
        pass # do nothing


def main():
    ts = TrafficSystem()
    # 100 time steps
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0.1)  # sleep 0.1 second
    print('\nFinal state:')
    ts.snapshot()
    print()
    ts.print_statistics()


if __name__ == '__main__':
    main()