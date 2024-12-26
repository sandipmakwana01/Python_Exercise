# Exercise: E001-V1
# •	Create one class named "category" with members "name", "code", "no_of_products"
# •	Create one class named "product" with members "name", "code", "category", "Price"
# •	Create three objects of a category.
# •	Create 10 different products. The code must be unique.
# •	Print category info with its no_of_products
# •	Sort and Print products based on price ( Price High to Low and Low to High) with all details.
# •	Search product using its code.

class Category:
    def __init__(self, name, code, no_of_products=0):
        self.name = name
        self.code = code
        self.no_of_products = no_of_products

    def category_info(self):
        print(f"Name : {self.name} | Code : {self.code} | No of Products : {self.no_of_products}")

class Product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price
        category.no_of_products += 1

    @staticmethod
    def sort_product(products):
        n = len(products)

        for i in range(n):
            for j in range(0, n - i - 1):
                if products[j].price > products[j + 1].price:  
                    products[j], products[j + 1] = products[j + 1], products[j]

        print("\nProduct Info (Low To High)")
        for product in products:
            print(f"Name : {product.name} | Code : {product.code} | Category : {product.category.name} | Price : {product.price}")

        for i in range(n):
            for j in range(0, n - i - 1):
                if products[j].price < products[j + 1].price:  
                    products[j], products[j + 1] = products[j + 1], products[j]
        
        print("\nProduct Info (High To low)")
        for product in products:
            print(f"Name : {product.name} | Code : {product.code} | Category : {product.category.name} | Price : {product.price}")
        
         
    @staticmethod
    def search_product(products):
        code = input("Enter code to find Product :")
        found = True
        for product in products:
            if product.code == code:
                print(f"Name : {product.name}\nCategory : {product.category.name}\nPrice : {product.price}")
                found = False
                break
        if found:
            print("Product no found.")

# •	Create three objects of a category.
c1 = Category("Electronics", "C1")
c2 = Category("Furniture", "C2")
c3 = Category("Clothing", "C3")

# •	Create 10 different products. The code must be unique.
p1 = Product("Laptop", "P1", c1, 1000)
p2 = Product("Smartphone", "P2", c1, 800)
p3 = Product("Tablet", "P3", c1, 600)
p4 = Product("Chair", "P4", c2, 100)
p5 = Product("Sofa", "P5", c2, 500)
p6 = Product("Table", "P6", c2, 200)
p7 = Product("T-Shirt", "P7", c3, 20)
p8 = Product("Jeans", "P8", c3, 40)
p9 = Product("Jacket", "P9", c3, 120)
p10 = Product("Shoes", "P10", c3, 80)

# •	Print category info with its no_of_products
print("Category Info")
c1.category_info()
c2.category_info()
c3.category_info()

# •	Sort and Print products based on price High to Low with all details.
ListOfProducts = [p1,p2,p3,p4,p5,p6,p7,p8,p9,p10]
Product.sort_product(ListOfProducts)

# •	Search product using its code.
Product.search_product(ListOfProducts)


       