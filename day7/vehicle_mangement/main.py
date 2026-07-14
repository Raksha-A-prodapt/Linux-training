from car import Car
from ev import EV
from polymosphism import overloading_demo
from exception import VehicleError
# car1=Car("toyato","Camry",2020)
# car2=Car("Honda","Civic",2015)
# car1.start_engine()
# car2.show_info()

# #encapsulation
# #print(car1.__owner) -- its privte
# car1.set_owner("Alice")

# #car1.set_owner("Bob")


# ev1=EV("Tesla",2021,-75)
# ev1.show_info()
# ev1.start_engine()
# ev1.charge_battery()
# overloading_demo()


from csv_report import  export_vehicle_data
def main():
    try:
        car1=Car("Toyata","Corolla",2022)
        car2=EV("Tesla","model 3",2023,75)
        car1.set_owner("Alice")
        car2.set_owner("Bob")
        vehicles= [car1,car2]
        print(car1.show_info(),car1.get_owner())
        print(car2.show_info,car2.get_owner())
        print("\n-----Overloading Demo-------")
        overloading_demo()
        print("\n----Overloading demo----")
        overloading_demo()
        print("\n---EXPORT Report------")
        print(export_vehicle_data("vehicle_report.csv",vehicles))
    except VehicleError as e:
        print(f"Error: {e}")
if __name__=="__main__":
    main()
    