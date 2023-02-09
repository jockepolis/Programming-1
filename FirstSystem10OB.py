from time import sleep

class Vehicle:
    """Represents vehicles in traffic simulations"""

    # Skapa ett fordon med födelsetid och en destination
    def __init__(self, destination, borntime):
        self.borntime = borntime
        self.destination = destination
    
    # Returnera destinationen och födelsetiden (f-sträng)
    def __str__(self):
        return f'Vehicle({self.destination}, {self.borntime})'


class Lane:
    "Represents a lane with (possible) vehicles"

    # Skapar fil med antal fordon som kan befinna sig på den
    def __init__(self, length):
        # Initiera alla element till 'None'
        self.the_lane = [None for x in range(length)]

    # Returnerar en lämplig strängrepresentation av objektet
    def __str__(self):
        res = ''
        for s in self.the_lane:
            if s == None:
                res = res + '.'
            else:
                res = res + s.destination
        return '[' + res + ']'

    # Lagrar fordonet v sist på filen om det är ledigt där annars returnera strängen i Exception''
    def enter(self, vehicle):
        if self.is_last_free():
            self.the_lane[-1] = vehicle
        else:
            raise Exception('Impossible to enter lane: position not free')

    # Är sista platsen i filen ledig? True or false
    def is_last_free(self):
        return self.the_lane[-1] == None

    # Flyttar alla fordon(utom det första) längre fram i filen, från vänster till höger
    def step(self):
        for i in range(len(self.the_lane)-1): # Första platsen "räknas" inte
            if self.the_lane[i] == None:
                self.the_lane[i] = self.the_lane[i+1]
                self.the_lane[i+1] = None

    # Returnerar fordonet längst fram i kön
    def get_first(self):
        return self.the_lane[0]

    # Returnerar och tar bort fordonet längst fram i kön
    def remove_first(self):
        v = self.the_lane[0]
        self.the_lane[0] = None
        return v

    # Returnerar antalet fordon dvs hur lång kön är i filen
    def number_in_lane(self):
        return len(self.the_lane) - self.the_lane.count(None)


class Light:
    """Represents a traffic light"""

    # Initiera och specicifiera egenskaperna
    def __init__(self, period, green_period):
        self.period = period
        self.green_period = green_period
        self.time = 0

    # Om grönt -> (G), om rött -> (R)
    def __str__(self):
        if self.is_green():
            return '(G)'
        else:
            return '(R)'

    # Interna klockan som är periodisk, då den är beroende av färgen på trafiksignalen
    def step(self):
        self.time = (self.time + 1) % self.period

    # Om (G) -> True, annars False
    def is_green(self):
        return self.time < self.green_period


# Copy Paste från uppgiften. Ger en sekvens av destinatoner för syd, väst o.s.v.
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


class TrafficSystem:
    """Defines a traffic system"""

    # Skapa trafiksystemet
    def __init__(self):
        self.time2 = 0
        self.lane1 = Lane(5) # Skapa två filer av längden 5 (fordon är enhet)
        self.lane2 = Lane(5)
        self.light = Light(7, 3) # Ansätt trafikljuset period och hur länge den är grön
        self.destination = Destinations() # Anropa Destinationsklassen
        self.queue = [] # Tom lista för kön

    # Metod som printar en ögonblicksbild för systemet baserat på de olika komponenterna i trafiksystemet
    def snapshot(self):
        """Prints a snapshot of the current state of the system"""
        print(f'{self.lane1} {self.light} {self.lane2}   {str([v.destination for v in self.queue])}')

    # Metod enligt beskrivning i uppgift som tar ett steg för alla komponenter i systemet
    def step(self):
        """Takes one step for all components in the system"""
        self.lane1.remove_first() # Ta bort första fordonet ur den vänstra filen
        self.lane1.step() # Stega den filen
        if self.light.is_green() is True:
            self.lane1.enter(self.lane2.remove_first()) # Om grönt, fordonen från lane 2 flyttas till lane 1
        self.light.step() # Stega signalen
        self.lane2.step() # Nu stega den högra filen
        destination = self.destination.step() # Anropa step-metoden i destinations
        if self.lane2.is_last_free() is True and len(self.queue) > 0: # Om sista platsen i lane2 är ledig och det finns någon i kön
            self.lane2.enter(self.queue.pop(0)) # Gå in i lane2 och ta bort den från kön
            if destination is not None: # Om destination returnerar en destination (dvs inte None)
                self.queue.append(Vehicle(destination, self.time2)) # Lägg till fordonet i kön
        elif self.lane2.is_last_free() is True and destination is not None: # Om sista platsen i lane2 är ledig och destination returnerar en destination
            self.lane2.enter(Vehicle(destination, self.time2)) # Lägg till den i lane2
        elif self.lane2.is_last_free() is False and destination is not None: # Men om sista platsen i lane2 är upptagen och destination returnerar en destination
            self.queue.append(Vehicle(destination, self.time2)) # Lägg fordonet sist i kön
        self.time2 += 1 # Sen har en tidsenhet gått

    # Dessa två metoder behövs inte i denna uppgift
    def number_in_system(self):
        pass

    def print_statistics(self):
        pass

# Copy Paste, printar systemets snapshots (ögonblicksbilder) för 100 tidsenheter
def main():
    ts = TrafficSystem()
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0.1)  # sleep 0.1 second
    ts.snapshot()
    print()

if __name__ == '__main__':
    main()