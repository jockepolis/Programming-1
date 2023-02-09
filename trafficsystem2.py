from destinations import Destinations
from trafficsystemcomponents import Light, Lane, Vehicle
from time import sleep
from statistics import mean, median                  #redovisat till niklas wik

class TrafficSystem:
    """Defines a traffic system"""

    def __init__(self):
        self.time = 0
        self.lane_new = Lane(11)
        self.lane_west = Lane(8)
        self.lane_south = Lane(8)
        self.W_after = Lane(3)
        self.S_after = Lane(3)
        self.light_west = Light(14, 6)
        self.light_south = Light(14, 4)
        self.destination = Destinations()
        self.queue = []
        self.stats_S = []
        self.stats_W = []
        self.number_vehicles = 0
        self.blocked = 0
        self.cars_in_queue = 0
        self.blockedind = ' '

    def snapshot(self):
        """Prints a snapshot of the current state of the system"""
        print(f'{self.time} : {self.W_after} {self.light_west} {self.lane_west}{self.blockedind}{self.lane_new}'    
              f'  {str([v.destination for v in self.queue])}\n'
              f'{self.S_after} {self.light_south} {self.lane_south}')

    def step(self):
        """Takes one step for all components in the system"""
        self.time += 1
        self.W_after.remove_first()
        self.S_after.remove_first()
        self.S_after.step()
        self.W_after.step()
        
        #move if green 
        if self.light_west.is_green():          
            moved = self.lane_west.remove_first()
            self.W_after.enter(moved)
            if moved is not None:
                self.stats_W.append(self.time - moved.get_borntime())     
        if self.light_south.is_green() is True:
            moved = self.lane_south.remove_first()
            self.S_after.enter(moved)
            if moved is not None:
                self.stats_S.append(self.time - moved.get_borntime())
        self.lane_west.step()
        self.lane_south.step()
        
        #entering either west or south depending on destination
        new = self.lane_new.get_first()   
        if new:
            if new.get_destination() == 'W':
                if self.lane_west.last_free():
                    self.lane_west.enter(self.lane_new.remove_first())
                else:
                    self.blocked += 1
                    self.blockedind = '*'
            elif new.get_destination() == 'S':
                if self.lane_south.last_free():
                    self.lane_south.enter(self.lane_new.remove_first())
                else:
                    self.blocked += 1
                    self.blockedind = '*'
        self.lane_new.step()
        self.light_west.step()
        self.light_south.step()

        destination = self.destination.step()
        if len(self.queue) > 0:
            self.cars_in_queue += 1
        if destination is not None:                               #om destination returnerar en destination
            self.queue.append(Vehicle(destination, self.time))        #lägg till en bil i kön
            self.number_vehicles += 1
        if self.lane_new.last_free() and len(self.queue) > 0:  #om sista platsen i laneWest är ledig och det finns någon i kön
            self.lane_new.enter(self.queue.pop(0))              #gå in i lane2 och ta bort från kön
                

        
    def in_system(self):
        """Return the number of vehicles in the system."""
        lanes = [self.lane_new, self.lane_west, self.lane_south]
        n_cars = len(self.queue)
        for v in lanes:
            n_cars += v.number_in_lane()     #metod i klassen lane
        return n_cars        


    def print_statistics(self):
        print(f'Statistics after {self.time} timesteps:\n\n'
              f'Created vehicles:\t {self.number_vehicles}\n'
              f'In system\t:\t  {self.in_system()}\n\n'
              f'At exit\t\t\tWest\t\t\tSouth\n'
              f'Vehicles out:\t\t{len(self.stats_W)}\t\t\t{len(self.stats_S)}\n'
              f'Minimal time:\t\t{min(self.stats_W)}\t\t\t{min(self.stats_S)}\n'
              f'Maximal time:\t\t{max(self.stats_W)}\t\t\t{max(self.stats_S)}\n'
              f'Mean time:\t\t{round(mean(self.stats_W),1)}\t\t\t{round(mean(self.stats_S),1)}\n'
              f'Median time:\t\t{round(median(self.stats_W),1)}\t\t\t{round(median(self.stats_S),1)}\n\n'
              f'Blocked:\t\t{round((self.blocked / self.time)*100,1)}%\n'
              f'Queue:\t\t\t{round((self.cars_in_queue / self.time) * 100, 1)}%'
              f'')


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
