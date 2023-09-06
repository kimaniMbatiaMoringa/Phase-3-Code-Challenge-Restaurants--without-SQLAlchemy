from classes.Review import Review
from classes.Customer import Customer
from classes.Restaurant import Restaurant

#Levels - Reviews calls the Customer class

import ipdb

restaurant1 = Restaurant("Mong Kok")

customer1 = Customer("Kimani", "Mbatia")

kims = Review(customer1,restaurant1,4)

ipdb.set_trace()