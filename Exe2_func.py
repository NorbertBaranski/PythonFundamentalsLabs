# Step 1 - Create a function
def calculate_sales(quantity, unit_price):
    return quantity * unit_price

result = calculate_sales(3, 1200.50) #call function with arguments
print("*** Sales Calculation using Function ***")
print("Total Sales:", result)

# Step 2 - Reuse the function with different values
print("*** Reusing Function with Different Values ***")
print("Total Sales for 5 units at $1500.75 each:", calculate_sales(5, 1500.75))
print("Total Sales for 2 units at $1500.75 each:", calculate_sales(2, 800))
print("Total Sales for 10 units at $1500.75 each:", calculate_sales(10, 250.25))

# Step 3 - Check and convert data types
print("")
print("Data Type Check and Conversion")
quantity = "5" # string variable
print("Original quantity (string):", quantity)
quantity = int(quantity) # convert string to integer
print("Coverd quantinty (int):", quantity)
print("Total Sales after conversion:", calculate_sales(quantity, 500)) # call function

# Step 4 – Store multiple values in a List
sales = [1200, 850, 2400, 1750, 3200]
print("")
print("****** Store multiple values in a  list")
print("Sales:", sales)
print("First sale:", sales[0]) #indexing
print("Number of sales:", len(sales))

# Step 5 – Create and process a Dictionary
order = {
    "OrderID": "ORD001", # key and value pair
    "Product": "Laptop",
    "Quantity": 2,
    "UnitPrice": 850
}
 
total = calculate_sales(order["Quantity"], order["UnitPrice"])
print("")
print("****** Create and Process a Dictionary ******")
print("Product:", order["Product"])
print("Total Sales:", total)