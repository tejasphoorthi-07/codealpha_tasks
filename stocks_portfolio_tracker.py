stock_prices = {
    "GOOGLE": 180,
    "MICROSOFT": 250,
    "VIVO": 140,
    "OPPO": 320,
    "SAMSUNG":440
}
total_investment = 0
n = int(input("Enter number of stocks: "))
for i in range(n):
    name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))
    if name in stock_prices:
        value = stock_prices[name] * quantity
        total_investment += value
        print(f"{name} Investment Value: ₹{value}")
    else:
        print("Stock not found!")
print("\nTotal Portfolio Value: ", total_investment)
