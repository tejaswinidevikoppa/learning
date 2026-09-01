customers = [
    {"name": "Alex", "age": 25, "city": "New York", "spend": 1200},
    {"name": "Sam", "age": 31, "city": "Boston", "spend": 850},
    {"name": "Jordan", "age": 22, "city": "New York", "spend": 1500},
    {"name": "Taylor", "age": 35, "city": "Chicago", "spend": 700},
    {"name": "Morgan", "age": 28, "city": "Boston", "spend": 1100},
]


total_customers = len(customers)
print("total_customers:", total_customers)

total_spending = 0 
for customer in customers:
    total_spending = total_spending + customer["spend"]

print("total_spending:", total_spending)

average_spending = total_spending / total_customers
print(average_spending)

highest_spending = 0
highest_spender = ""

for customer in customers:
    if customer["spend"] > highest_spending:
        highest_spending = customer["spend"]
        highest_spender = customer["name"]

print(highest_spender)
print(highest_spending)        

New_York_count = 0
for customer in customers:
    if customer["city"] == "New York":
        New_York_count = New_York_count + 1

print(New_York_count)        

high_spending_customers = [ ]
for customer in customers:
    if customer["spend"] > 1000 :
        high_spending_customers.append(customer["name"])

print(high_spending_customers)        