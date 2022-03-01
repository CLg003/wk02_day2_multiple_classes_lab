class Bus:
    def __init__(self, route, destination):
        self.route_number = route
        self.destination = destination
        self.passengers = []
    def drive(self):
        return 'Brum brum'
    def passenger_count(self):
        return len(self.passengers)
    def pick_up(self, person):
        self.passengers.append(person)
    def drop_off(self, person):
        self.passengers.remove(person)
    def empty(self):
        self.passengers = []
    def pick_up_from_stop(self, bus_stop):
        for person in range(len(bus_stop.queue)):
            self.pick_up(person)
        bus_stop.clear

