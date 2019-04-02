
def menu():
    print("Welcome, please choose from the options below:")
    print("1. Book a flight for a passenger")
    print("2. See all passangers on a flight")
    print("3. See al flights in a terminal")
    print("4. Add aircraft to flight")
    print("5. Change aircraft")
    print("7. Cancel flight")
    print("6. Exit")
    print(" ")
    return input ("Choose your option: ")

print(menu())

class Airport:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Terminal:
    def __init__(self, name, number_of_gates, gates_names):
        self.name = name
        self.number_of_gates = number_of_gates
        self.gates_names = gates_names

class Flights:
    def __init__(self, flight_number, flight_date, scheduled_time):
        self.flight_number = flight_number
        self.flight_date = flight_date
        self.scheduled_time = scheduled_time

