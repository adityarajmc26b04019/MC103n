class car: # class
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def print_name(self):
        print(f"{self.brand} {self.model} {self.year}")
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kms on it")
    def update_odometer(self,reading):
        self.odometer_reading = reading
    def travel(self, distance_travelled):
        self.odometer_reading += distance_travelled
    def mileage(self, fuel_used):
        print(f"Mileage is {(self.odometer_reading/fuel_used):.2f} km/l")

my_car = car('Audi','A8',2010) # Objects
my_car.print_name()
my_car.update_odometer(2000)
my_car.read_odometer()
my_car.travel(123)
my_car.read_odometer()
my_car.mileage(145)

# create a method that adding the distance fromm a journey to the odometer reading and updates it
# calculate milage based on total distance vs fuel consumed 

# class Electric_car(car): # subclass
#     def __init__(self,brand,model,year,battery_size):
#         super().__init__(brand,model,year)
#         self.odometer_reading = 0
#         self.battery_size = battery_size # in kwh
#     def battery_left(self, percentage_battery_used):
#         print(f"{100-percentage_battery_used}% is left.")
#     def mileage(self, battery_used_in_kwh):
#         print(f"{self.odometer_reading/battery_used_in_kwh} is Mileage.")



# my_evcar = Electric_car('Mercedes','D10',2028, 1200)
# my_evcar.print_name()
# my_evcar.travel(123)
# my_evcar.read_odometer()
# my_evcar.mileage(145)
# my_evcar.battery_left(23)