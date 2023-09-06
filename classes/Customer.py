import gc
from classes.Review import Review

class Customer:
    instances=[]

    def __init__(self,name, family_name):
        self.name =name
        self.family_name = family_name
        self.instances.append(self)

    def given_name(self):
        return self.name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return self.name + " " + self.family_name
    
    def __str__(self) -> str:
        return f"Name: {self.name}"
    
    def all(self):
        for item in self.instances:
            print(item.name)

    def add_review(self,restaurant, rating):
         review = Review(self.name,restaurant,rating)
         restaurant.add_customer(self.full_name())
         return review.customer()       
    
"""     def all(of_class):
        _instances = []
        for obj in gc.get_objects():
            if isinstance(obj, of_class):
                _instances.append(obj) """

