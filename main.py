from datetime import datetime
import csv, time, sys

from unicodedata import category


def add_transaction():
    """
    Returns: transaction [date/ int / str/ str]
    """
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
            print("This is not a number!")



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

def show_transaction(r):
    for idx, tr in enumerate(r):
        print(f'{idx+1}. Date: {tr["date"]} | Amount: ${float(tr["amount"]):.2f} | Category: {tr["category"]} | Description: {tr["description"]}')


while True:
    print("#" * 10)
    print("|-|-| Transaction Menu |-|-| \n")
    options_list = ["Add a transaction", "View all transactions", "Transactions Summary","Filter Transactions","Exit"]

    for index, option in enumerate(options_list):
        print(f"{index + 1}. {option}")

    command = input("Enter your choice: ").strip()
    if command == "1":
        csv_fields = ['date', 'amount', 'category', 'description']
        rows = []
        with open("transactions.csv", "a+", newline='') as csv_file:

            csv_file.seek(0)  # set poiter to top of the page
            first_line = csv_file.readline()
            csv_writer = csv.writer(csv_file)

            if first_line.strip() == '':
                csv_writer.writerow(csv_fields)

            start_transaction_storage = input("Would you like to add your transaction (y/n)? ").strip().lower()
            while True:
                if start_transaction_storage.lower() != 'y':
                    print("Returning to menu...")
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

    elif command == "2":
        try:
            with open("transactions.csv", "r+", newline='') as csv_read_file:
                read_content = csv.DictReader(csv_read_file)

                read_rows = list(read_content)
                if not read_rows:
                    print("No transactions found.")
                else:
                    show_transaction(read_rows)
        except IOError as e:
            print(f"Error reading file: {e}")

    elif command == "3":
        try:
            with open("transactions.csv","r", newline='') as csv_summary:
                read_content = csv.DictReader(csv_summary)
                read_rows = list(read_content)

                total_expense = float(0)
                total_income = float(0)


                if not read_rows:
                    print("No transactions found.")
                else:
                    for row in read_rows:
                        t_amount = float(row["amount"])
                        if row["category"] == "expense":
                            total_expense += t_amount
                        else:
                            total_income += t_amount
                net_balance = total_income - total_expense

                print("\n")
                print("## Transaction summary ##")
                print(f'Total Income: ${total_income:.2f}')
                print(f'Total Expense: ${total_expense:.2f}')
                print(f'Total Balance: ${net_balance:.2f}')
                print("\n")


        except IOError as err:
            print(f"Error reading file: {e}")
    elif command == "4":
        try:
            with open("transactions.csv", "r", newline='') as csv_filter:
                read_content = csv.DictReader(csv_filter)
                read_rows = list(read_content)
                if not read_rows:
                    print("No transactions found.")
                    continue

                filters = ["category", "amount", "date", "description", "exit"]



                while True:
                    print('\nTransaction filters:')
                    for i, fil in enumerate(filters):
                        print(f"{i + 1}. {fil}")
                    filter_choice = input("Choose a filter: ").strip().lower()
                    if filter_choice == "category":
                        category_choice = input("Choose a category(expense/income): ")
                        for idx, tr in enumerate(read_rows):
                            if tr["category"] == category_choice:
                                print(f'{idx + 1}. Date: {tr["date"]} | Amount: ${float(tr["amount"]):.2f} | Category: {tr["category"]} | Description: {tr["description"]}')

                    elif filter_choice == "exit":
                        print("Going back to menu...")
                        break
                    else:
                        print("Invalid choice, try again.")

        except IOError as e:
            print(f"Error reading file: {e}")

    elif command == "5":
        print("Exiting program...")
        for i in range(3,0,-1):
            time.sleep(1)
            print(f"{i}...")
        break
    else:
        print("Invalid command. Try again.")


