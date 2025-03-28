from datetime import datetime


def add_transaction():
    transaction = {}
    date_format = '%Y-%m-%d'

    print("Please input the details of your transaction")
    while True:
        try:
            date = input("Enter the date (YYYY-mm-dd): ")
            date = datetime.strptime(date,date_format).date()
            break
        except ValueError:
            print("Invalid date. Please use the format YYYY-MM-DD.")

    while True:
        try:
            amount = float(input("Enter the transaction amount(positive only): "))
            if amount < 0:
                print("Enter only positive amounts: ")
                continue
            break
        except ValueError:
            print("It is not a number!")



    categories = ["expense","income"]
    category = input("Enter the transaction category(expense/income): ").lower()
    while category not in categories:
        category = input("Enter the transaction category(expense/income): ")
    if category == "expense":
        amount = 0 - amount

    description = input("Enter transaction description: ")
    while len(description) < 5 or description.isnumeric():
        description = input("Description is too short. Please enter the appropiate description:")


    transaction["date"] = date
    transaction["amount"] = amount
    transaction["category"] = category
    transaction["description"] = description


    return transaction

print(add_transaction())


