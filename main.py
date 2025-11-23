# Expense Tracker Project

expenses = [] # list of expenses in form of dictionaries

print("Welcome to Expense Tacker 💵")

while True:

    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View total Expense")
    print("4. Exit")

    choice = int(input("Please Enter your choice (1-4): "))

# Add Expenses 
    if(choice == 1):
        date = input("Enter your date of enxpense : ")
        category = input("Enter your category of expense : ")
        description = input("Description : ")
        amount = float(input("Enter the amount : "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(expense)
        print("\nExpenses added succesfully")

# View all Expenses         
    elif(choice == 2):
        if (len(expenses)==0):
            print("No Expenses Added. Now first spend some Money Bro")
        else:
            print("====Here are your Expenses====")
            count = 1
            for item in expenses:
                print(f"Expense No. {count} -> {item['date']}, {item['category']}, {item['description']}, {item['amount']}")

                count += 1

# View total spending
    elif(choice == 3):
        total = 0
        for item in expenses:
            total = total + item["amount"]

        print("\n Total expense = ",total)   

# Exit
    elif(choice == 4):
        print("Thank you for using our system")
        break

    else:
        print("Invalid choice..Try again")