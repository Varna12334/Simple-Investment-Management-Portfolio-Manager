import csv
import os

FILE_NAME = "data.csv"

def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Amount Invested", "Current Value"])

def add_investment():
    name = input("Enter investment name: ")
    invested = float(input("Enter amount invested: "))
    current = float(input("Enter current value: "))

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, invested, current])

    print("✅ Investment added successfully!\n")

def view_portfolio():
    total_invested = 0
    total_current = 0

    print("\n📊 Portfolio Summary")
    print("-" * 55)
    print("Name | Invested | Current | P/L | P/L %")
    print("-" * 55)

    with open(FILE_NAME, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            invested = float(row["Amount Invested"])
            current = float(row["Current Value"])

            profit = current - invested
            percent = (profit / invested) * 100 if invested != 0 else 0

            total_invested += invested
            total_current += current

            print(f"{row['Name']} | ₹{invested} | ₹{current} | ₹{profit} | {percent:.2f}%")

    print("-" * 55)
    print(f"Total Invested: ₹{total_invested}")
    print(f"Current Value: ₹{total_current}")
    print(f"Overall Profit/Loss: ₹{total_current - total_invested}\n")

def menu():
    print("💰 Investment Portfolio Manager")
    print("1. Add Investment")
    print("2. View Portfolio")
    print("3. Exit")

init_file()

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        add_investment()
    elif choice == "2":
        view_portfolio()
    elif choice == "3":
        print("👋 Exiting... Thank you!")
        break
    else:
        print("❌ Invalid choice\n")
