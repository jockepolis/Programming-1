#  Klassen Destinations,  2020-11-12
class Destinations:
    """ Generates a sequence of destinations (None, 'W', 'S') """

    def __init__(self):
        """Add internal data."""
        self._arrivals = (  # 0:52, 1:26, 2:22
            # 0->None, no vehicle, 1->a vehicle with destination W
            # 2->a vehicle with destination S
            2, 2, 2, 2, 2, 1, 2, 2, 2, 1, 1, 2, 1, 2, 2, 2, 1, 2, 1, 1,
            2, 1, 1, 0, 2, 0, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 0, 2, 0, 1,
            2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1,
            0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 2, 0, 0,
            1, 2, 0, 1, 0, 2, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1)

        self._internal_time = 0
        self._total_cycle = len(self._arrivals)

    def step(self):
        """Make one time step, reporting the desination of the next vehicle
        (or None)."""
        ind = self._arrivals[self._internal_time]
        self._internal_time = (self._internal_time + 1) % len(self._arrivals)
        # if == 1 -> W, if == 2 -> S, else -> None
        return 'W' if ind == 1 else 'S' if ind == 2 else None
    
    
def main():
    """Demonstrates the class destination"""
    dest = Destinations()
    print('The first 50 destinations...')
    for i in range(50):
        if (i+1) % 20 != 0:
            print(f'{dest.step()},', end ='')
        else:
            print(f'{dest.step()}')
    

if __name__ == '__main__':  # If this file is the main program, you are running:
    main()                  # Call the main function above