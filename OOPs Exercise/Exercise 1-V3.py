# Exercise: E001-V3: 
# Create one class named “location” with members “name”, “code”. 
# Create one class named “movement” with members “from_location”, “to_location”, “product”, “quantity”.

# Create one static method named “movements_by_product” inside the “movement” class with one argument named “product”. 
# This method will return all “movement” objects {which belong to the passed} “product” as an argument.

# Add new members inside the product “stock_at_locations”. 
# This new member is a type of Dictionary 
# and it contains “location” as key 
# and actual stock of that product on that location as value.

# Create 4 different location objects.
# Create 5 different product objects.
# Move those 5 products from one location to another location using movement. [Manage exceptions if product stock goes in -ve.]
#  
# Display movements of each product using the “movement_by_product” method.
# Display product details with its stock at various locations using “stock_at_locations”.
# Display product list by location (group by location).

class Location:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class Product:
    def __init__(self, name):
        self.name = name
        self.stock_at_locations = {}    

    def display_stock_at_locations(self):
        print(f"{self.name}:")
        for location, stock in self.stock_at_locations.items():
            print(f"  - {location.name}: {stock}")

    def display_movements(self):
        print(f"{self.name}:")
        movements = Movement.movements_by_product(self)
        for movement in movements:
            print(f"  - {movement.from_location.name} ==> {movement.to_location.name} | Quantity: {movement.quantity}")
        # pass

    @staticmethod
    def display_products_by_location(products): 
        print("\nProduct list by location:")
        location_product = {}
        for product in products:
            for location, stock in product.stock_at_locations.items():
                if location not in location_product:
                    location_product[location] = []
                location_product[location].append((product.name, stock))

        # return location_product
        for location, products in location_product.items():
            print(f"{location.name}:")
            for product, stock in products:
                print(f"  - Product : {product} | Quantity : {stock}")

class Movement:
    movements = []

    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity

        if product.stock_at_locations.get(from_location) < quantity:
            raise ValueError(f" \nNot availbe {product.name} in {from_location.name}. Available: {product.stock_at_locations.get(from_location)}, Required: {quantity}.")
            
        product.stock_at_locations[from_location] -= quantity
        product.stock_at_locations[to_location] = product.stock_at_locations.get(to_location) + quantity

        Movement.movements.append(self)

    @staticmethod
    def movements_by_product(product):
        result = [] 
        for movement in Movement.movements:  
            if movement.product == product:  
                result.append(movement)
        return result 

   
# Create locations
location1 = Location("India", "L1")
location2 = Location("China", "L2")
location3 = Location("Indonesia", "L3")
location4 = Location("Pakistan", "L4")

# Create products
product1 = Product("Vehicle")
product2 = Product("Electronics")
product3 = Product("Furniture")
product4 = Product("Clothing")
product5 = Product("Oil Truck")

# Initialize stock at locations
for product in [product1, product2, product3, product4, product5]:
    product.stock_at_locations[location1] = 100
    product.stock_at_locations[location2] = 0
    product.stock_at_locations[location3] = 40
    product.stock_at_locations[location4] = 0

# Display stock at various locations for each product
print("\nProduct details with stock at various locations:")
for product in [product1, product2, product3, product4, product5]:
    product.display_stock_at_locations()

# Perform movements
try:
    Movement(location1, location2, product1, 50)
    # Movement(location3, location4, product2, 30)
    # Movement(location1, location4, product3, 70)
    # Movement(location2, location4, product1, 20)
    Movement(location3, location2, product2, 45)
except ValueError as e:
    print(e)


# Display movements for each product
print("\nMovements of each product:")
for product in [product1, product2, product3, product4, product5]:
    product.display_movements()

# Display product list by location
Product.display_products_by_location([product1, product2, product3, product4, product5])
