stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 135
}

investment = 0
portfolio = []

n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock = input("\nEnter stock name (AAPL, TSLA, GOOGL, MSFT, AMZN): ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock] * quantity
        investment += investment

        portfolio.append([stock, quantity, stock_prices[stock], investment])

    else:
        print("Stock not found!")

print("\n----- STOCK PORTFOLIO -----")
print("{:<10}{:<10}{:<12}{:<15}".format("Stock", "Qty", "Price", "Investment"))

for item in portfolio:
    print("{:<10}{:<10}{:<12}${:<15}".format(item[0], item[1], item[2], item[3]))

print("\nTotal Investment = $", investment)


file=open("portfolio.txt", "w")
file.write("Stock Portfolio\n")
file.write("-------------------------------\n")

for item in portfolio:
    file.write(f"{item[0]}  Qty:{item[1]}  Price:${item[2]}  Investment:${item[3]}\n")

file.write(f"\nTotal Investment = ${investment}")

print("\nPortfolio saved successfully to 'portfolio.txt'")
