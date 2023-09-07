from classes.Review import Review
from classes.Customer import Customer
from classes.Restaurant import Restaurant

#Levels - Reviews calls the Customer class

import ipdb

restaurant1 = Restaurant("Mong Kok")

customer1 = Customer("Kimani", "Mbatia")
customer2 = Customer("John", "Obath")

customer1.add_review(restaurant1,4)
customer2.add_review(restaurant1,2)

kims = Review(customer1,restaurant1,1)

ipdb.set_trace()