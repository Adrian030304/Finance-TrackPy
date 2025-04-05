from datetime import datetime
import csv, time, sys

def add_transaction():
    '''
    Returns: transaction [date/ int / str/ str]
    '''
    transaction_data = {}
    date_format = '%Y-%m-%d'

    print("Please input the details of your transaction")
    while True:
        try:
            date = input("Enter the date (YYYY-mm-dd): ")
            date = datetime.strptime(date,date_format).date().isoformat()
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

    description = input("Enter transaction description: ")
    while len(description) < 5 or description.isnumeric():
        description = input("Description is too short. Please enter the appropriate description:")


    transaction_data["date"] = date
    transaction_data["amount"] = amount
    transaction_data["category"] = category
    transaction_data["description"] = description


    return transaction_data

csv_fields = ['date','amount','category','description']
rows = []

with open("transactions.csv","a+", newline='') as csv_file:

    csv_file.seek(0) #set poiter to top of the page
    first_line = csv_file.readline()
    csv_writer = csv.writer(csv_file)

    if first_line.strip() == '':
        csv_writer.writerow(csv_fields)

    start_transaction_storage = input("Would you like to note your transaction (y/n)? ")
    while True:
        if start_transaction_storage.lower() != 'y':
            print("Exiting program...")
            time.sleep(1)
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            break
        transaction = add_transaction()
        transaction_values = [transaction[field] for field in transaction]

        rows.append(transaction_values)
        start_transaction_storage = input("Would you like to add another transaction (y/n)? ")
    csv_writer.writerows(rows)



with open("transactions.csv","r+",newline='') as csv_read_file:
    pass



