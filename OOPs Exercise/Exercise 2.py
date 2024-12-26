from datetime import date , datetime
# Exercise: E002
#Create a new class named "Customer" with below members. "name","email","phone","street","city","state","country","company","type".
#"type" must be from "company,contact,billing,shipping".
#"Company" must be a Customer object which is the parent object.
#Apply Multiple possible validation for phone number and email
#Does not allowed number in name,city,state and country

#Create a new class named "Order" with members "number","date", "company", "billing", "shipping", "total_amount","order_lines".
#"company", "billing", "shipping" are objects of Customer.
#"date" must be today or the future. Does not allow past date.
#"total_amount" auto calculated based on different products inside order.
#"order_lines" is list of objects of "OrderLine"

#create a new class named "OrderLine" with members "order", "product", "quantity", "price", "subtotal".
#"order" is the object of Order.
#"subtotal" is auto calculated based on quantity and price.

#Display Order and Customer Information
#Sort orders based on "date".
#User can filter the current month orders
#Search Orders from its number.
#List/Display all orders of a specific product.

class Customer:
    def __init__(self,name,email,phone,street,city,state,country,type=None):
        self.name = name 
        self.email = email
        self.phone = phone
        self.street = street
        self.city = city 
        self.state = state 
        self.country = country
        self.type = type
        self.validate()

    def validate(self):
        string = self.name + self.city + self.state + self.country
        for i in string:
            if i in '0123456789':
                raise ValueError("The string contains numbers, which are not allowed.")

        if "@" not in self.email or "." not in self.email:
            raise ValueError("Email is not valid please check email.")

        if len(self.phone) not in [10, 13]:
            raise ValueError("Incorect Phone Number please check phone number")

        type_must_be = ["company","contact","billing","shipping"]
        if self.type not in type_must_be:
            raise ValueError("Invalid type.")

       
class Order:
    def __init__(self,number,date,company,billing,shipping,order_lines):
        self.number = number
        self.date = date
        self.company = company
        self.billing = billing
        self.shipping = shipping
        self.order_lines = order_lines
        self.total_amount = self.total_amounts()
        self.validate()

    def validate(self):
        if self.date < date.today():
            raise ValueError("Date must be today or the future. Does not allow past date.")
        
    def total_amounts(self):
        total = 0
        for i in self.order_lines:
            total += i.subtotal
        return total

    def dispaly_order_customer_info(self):
        print("Customer :")
        print(f"- Name : {self.billing.name}")
        print(f"- Email : {self.billing.email}")
        print(f"- Phone : {self.billing.phone}")
        print(f"- Address : {self.billing.street}, {self.billing.city}, {self.billing.state}, {self.billing.country}")
        print("\nOrder :")
        print(f"- Number : {self.number}")
        print(f"- Date : {self.date}")
        print(f"- Company : {self.company.name}")
        print("- Billing Address:", self.billing.street)
        print("- Shipping Address:", self.shipping.street)
        for i in self.order_lines:
            print(f"  -  {i.product} | Quantity:  {i.quantity} | Price : {i.price} | Subtotal: {i.subtotal}")
        print(f"                                      - Total amount : {self.total_amount}")


    def sort_orders_by_date(orders):
        for i in range(len(orders)):
            for j in range(i + 1, len(orders)):
                if orders[i].date > orders[j].date:
                    orders[i], orders[j] = orders[j], orders[i]
       
        for order in orders:
            print(f"Order Number: {order.number}, Date: {order.date}")
  
    def filter_current_month_orders(orders):
        current_month = datetime.now().month
        current_year = datetime.now().year

        for i in orders:
            if i.date.month == current_month and i.date.year == current_year:
                print(f"Order Number: {i.number}, Date: {i.date}")

    def search_order_by_number(orders):
        order_number = int(input("Enter Order Number to search Order: "))
        found = True
        for i in orders:
            if i.number == order_number:
                print(f"Order Number : {i.number} | Date : {i.date} | Total amount : {i.total_amount}")
                found = False
                break
        if found:
            print("Order Not Found.")

    def list_orders_by_product(orders):
        product_name = input("Enter the spacific product name: ")
        found = False
        for order in orders:
            for order_line in order.order_lines:
                if order_line.product.lower() == product_name.lower():
                    found = True
                    print(f"Order Number: {order.number}, Date: {order.date}, Total amount: {order.total_amount}")
                    break 
        if not found:
            print("No orders found with the specified product.")

class OrderLine: 
    def __init__(self,order,product,quantity,price):
        self.order = order
        self.product = product
        self.quantity = quantity
        self.price = price
        self.subtotal = self.price * self.quantity

company = Customer("Flipkart","flipkart@gmail.com","+910123456789","184 street","Ahemdabad","Gujarat","India",type="company")

customer1 = Customer("Vivek Roy","vivek@gmail.com","9876543210","Akash vani","Rajkot","Gujarat","India",type="contact")
order_line1 = OrderLine(None,"Product 1",2,100) 
order_line2 = OrderLine(None,"Product 2",1,500)
order1 = Order(284,date(2025,12,24),company,customer1,customer1,order_lines=[order_line1,order_line2])
order_line1.order = order1
order_line2.order = order1

customer2 = Customer("Rahul Makwana","rahul@gmail.com","1234567789","Shita ram park","Rajkot","Gujarat","India",type="contact")
order_line2 = OrderLine(None,"Product 6",1,700) 
order_line4 = OrderLine(None,"Product 1",7,100)
order2 = Order(826,date(2024,12,25),company,customer2,customer2,order_lines=[order_line2,order_line4])
order_line2.order = order2
order_line4.order = order2

orders = [order1,order2]

print("\n---Display Order and Customer Information---")
for order in orders:
    order.dispaly_order_customer_info()

print("\n---Sort orders based on date---")
Order.sort_orders_by_date(orders)

print("\n---Filter the current month orders---")
Order.filter_current_month_orders(orders)

print("\n---Search order by number---")
Order.search_order_by_number(orders)

print("\n---List/Display all orders of a specific product---")
Order.list_orders_by_product(orders)






# while True:
#     print("\n---Display Order and Customer Information---")
#     for order in orders:
#         order.dispaly_order_customer_info()
    
#     print("\n---Sort orders based on date---")
#     Order.sort_orders_by_date(orders)
    
#     print("\n---Filter the current month orders---")
#     Order.filter_current_month_orders(orders)

#     user_input = input("""
# 1. Search order by number 
# 2. List/Display all orders of a specific product
# 3. Exit program 
#             Enter number of choice : """)
    
#     if user_input == "3":
#         break
#     elif user_input == "1":
#         print("\n---Search order by number---")
#         Order.search_order_by_number(orders)
#     elif user_input == "2":
#         print("\n---List/Display all orders of a specific product---")
#         Order.list_orders_by_product(orders)
#     else:
#         print("Enter valide choice")




