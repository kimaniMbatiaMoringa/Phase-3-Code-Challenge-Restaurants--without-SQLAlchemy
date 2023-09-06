from classes.Review import Review
from classes.Customer import Customer
from classes.Restaurant import Restaurant

#Levels - Reviews calls the Customer class

import ipdb

restaurant1 = Restaurant("Mong Kok")

customer1 = Customer("Kimani", "Mbatia")
customer2 = Customer("John", "Obath")

#kims = Review(customer1,restaurant1,4)
#johns = Review(customer2, restaurant1,2)

kims = Customer.add_review(customer1,restaurant1,4)
johns = Customer.add_review(customer2,restaurant1,2)

ipdb.set_trace()