class Restaurant:
    """A simple restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.name=restaurant_name
        self.type=cuisine_type
        self.number_served=0

    def open_restaurant(self):
        print(f"{self.name} is now open.")

    def describe_restaurant(self):
        print(f"Name: {self.name} has cuisine type: {self.type}.")

    def set_number_served(self, number_served):
        if number_served < self.number_served:
            print(f"you cannot have less number served than before")
        else:
            self.number_served=number_served
        

    def increment_number_served(self, add_to):
        self.number_served+=add_to


class Icecream_Stand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Icecream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors=["blueberry", "strawberry","chocolate"]

    def describe(self):
        print (f"{self.name} carries the following flavors")
        for name in self.flavors:
            print(f"\t{name}")

'''
rest1 = Restaurant("Billy Joes", "BBQ")
rest1.describe_restaurant()
rest1.open_restaurant()
rest2 = Restaurant("Charlies", "Tacos")
rest2.describe_restaurant()
rest2.open_restaurant()
rest3 = Restaurant("Outback", "Steak House")
rest3.describe_restaurant()
rest3.open_restaurant()

print(f"{rest2.name} served {rest2.number_served}")
rest2.set_number_served(50)
print(f"{rest2.name} served {rest2.number_served}")
rest2.set_number_served(49)
print(f"{rest2.name} served {rest2.number_served}")
rest2.increment_number_served(10)
print(f"{rest2.name} served {rest2.number_served}")
'''

