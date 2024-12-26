# Exercise: E001-V2
# •	Add new data members “parent”, “display_name”, and “products” (list of product objects) inside the category class.
# •	Add a new member function to generate “display_name”.
# •	“display_name” has the text value as below.
# 1.	Vehicle category without parent then “Vehicle” 
# 2.	Car category with “Vehicle” as a parent then “Vehicle > Car”
# 3.	Petrol category with “Car” as a parent then “Vehicle > Car > Petrol”
# •	Create 5 category objects with parent and child relation.
# •	Create 3 product objects in each category.
# •	Display Category with its Code, Display Name and all product details inside that category.
# •	Display product list by category (group by category, order by category name).

class Category:
    def __init__(self, name, code, parent=None):
        self.name = name
        self.code = code
        self.parent = parent
        self.display_name = self.generate_display_name()
        self.products = [] 

    def generate_display_name(self):
        name = self.name 
        parent = self.parent

        while parent:
            name = f"{parent.name} > {name}"
            parent = parent.parent

        return name

    @staticmethod
    def display_category(categories):
        print("Category and Product Details:")
        for category in categories:
            print(f"\nCategory Code: {category.code}")
            print(f"Display Name : {category.display_name}")
            print("Products:")
            for i in category.products:
                print(f" - Name : {i.name} | Code : {i.code} | Price : {i.price}")

    @staticmethod
    def display_product(categories):
        n = len(categories)

        for i in range(n):
            for j in range(0,n-i-1):
                if categories[j].name > categories[j + 1].name:
                    categories[j] , categories[j +1] = categories[j+1] , categories[j]

        print("\n\nProducts Ordered by Category Name:")
        for category in categories:
            print(f"{category.name}")
            for product in category.products:
                print(f"  - Name : {product.name} | Code: {product.code} | Price: {product.price})")        
      
class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price
        category.products.append(self)

vehicle = Category("vehicle", "C1")
car = Category("car", "C2", parent=vehicle)
petrol = Category("petrol", "C3", parent=car)
furniture = Category("furniture", "C4")
electronics = Category("electronics", "C5")

p1 = Product("BMW", "P1", car, 15000)
p2 = Product("Creta", "P2", car, 25000)
p3 = Product("Cng", "P3", car, 12000)

p4 = Product("Fuel", "P4", petrol, 800)
p5 = Product("Oil", "P5", petrol, 100)
p6 = Product("Ges", "P6", petrol, 500)

p7 = Product("Sofa", "P7", furniture, 200)
p8 = Product("Table", "P8", furniture, 150)
p9 = Product("Chair", "P9", furniture, 50)

p10 = Product("Laptop", "P10", electronics, 1000)
p11 = Product("Smartphone", "P11", electronics, 800)
p12 = Product("Tablet", "P12", electronics, 600)

p7 = Product("Sofa", "P7", vehicle, 200)
p8 = Product("Table", "P8", vehicle, 150)
p9 = Product("Chair", "P9", vehicle, 50)

categories = [vehicle, car, petrol, furniture, electronics]

Category.display_category(categories)
Category.display_product(categories)







