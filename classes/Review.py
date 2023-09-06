from classes.Customer import Customer

class Review:
    def __init__(self,customer,restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

    def customer(self):
        return self.customer
        
    def rating(self, restaurant):
        pass
    
"""     def get_customer(self):
        return self.customer """
    
"""     def set_customer(self,value):
        if type(value) == str:
            print("Valid input")
            self._customer = value """

    #customer = property(fget=get_customer,fset=set_customer)        

