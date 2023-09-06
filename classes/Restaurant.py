from functools import reduce

class Restaurant:   
    def __init__(self,name):
        self.name = name
        self.ratings = []
        self.agg = 0

    def name(self):
        return self.name
    
    def get_rating(self):
        self.agg =reduce(sum,self.ratings)
    
    def set_rating(self,value):
        input = value
        self.ratings.append(input)