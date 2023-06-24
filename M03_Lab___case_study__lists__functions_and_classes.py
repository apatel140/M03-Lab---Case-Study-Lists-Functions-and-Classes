class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
       
        
      def set_year(self, year):
          self.__year = year
      def set_make(self, make):
          self.__make = make
      def set_model(self, model):
          self.__model = model 
      def set_doors(self, doors):
          self.__doors = doors
      def self_roof(self, roof):
          self.__roof = roof


def main(): 
#prompts the user
year = input("Enter year: ")
make = input("Enter make: ")
model = input("Enter model: ")
doors = input("Enter number of doors (2 or 4): ")
roof = input("Enter roof (solid or sun roof): ")

car = Automobile("car", year, make, model, doors, roof)

print("Vehicle type: ")
print("Year: " )
print("Make: " )
print("Model: " )
print("Number of doors: " )
print("Type of roof: " )
 