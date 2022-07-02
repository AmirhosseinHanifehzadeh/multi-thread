from food import *

class Restaurant:
    def __init__(self, name, district, catagory, address, manager_name):
        self.name = name 
        self.district = district 
        self.catagory = catagory
        self.address = address
        self.manager_name = manager_name
        self.foods = []

    def add_food(self, wanted_food, wanted_food_stock):
        for food in self.foods:
            if wanted_food == food['food'].name:
                food['stock'] += wanted_food_stock      
                return 

    def add_new_food(self,name, material, fixed_price, customer_price, category, stock):
        wanted_food = Food(name, material, fixed_price, customer_price, category)
        self.foods.append({
            'food': wanted_food,
            'stock': stock
        })

    def buy_food(self, wanted_food, wanted_number):
        for food in self.foods: 
            if food['food'].name == wanted_food:
                food['stock'] -= wanted_number

    
    def edit_restaurant(self, name, district, catagory, address, manager_name):
        self.name = name 
        self.district = district
        self.catagory = catagory 
        self.address = address
        self.manager_name = manager_name 
        
