class Car:
    def __init__(self,year,model,make):
        self.year=year
        self.model=model
        self.make=make 
        self.odometer_reading=200

    def get_car_description(self):
        full_name=f"{self.year} {self.model} {self.make}"
        return full_name
    def read_odometer(self):
        print(f"This car has an odometer reading of : {self.odometer_reading} miles on it.")

    def update_odometer_reading(self,mileage):
        if mileage >=self.odometer_reading:
            odometer_reading=mileage
        else :
            print("The odometer can not be Rolled back! ")
    def increment_odometer(self,miles):
        self.odometer_reading+=miles

My_car=Car('2000',"Toyota","Camry") 

print(My_car.get_car_description())
My_car.read_odometer()
My_car.increment_odometer(50)
My_car.read_odometer()
My_car.update_odometer_reading(205)
My_car.read_odometer()

