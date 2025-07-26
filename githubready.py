import os
import time
transactions = []
k=0

print("-----WELCOME TO DA BANK-------")

def show_menu():
   time.sleep(0.5)
   print("\n-----MENU-----")
   print("1. Add a trasaction")
   print("2. View all transactions")
   print("3. View Summary")
   print("4. Use ai advice")
   print("5. Exit")
   
def add_transaction():
     while True:
        try:
            amount = float(input("Enter the amount: "))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        while True:
            try:
                category = int(input("Enter the category (1 = income, 2 = expenses): "))
                if category == 1:
                    time.sleep(1)
                    print("income chosen")
                    time.sleep(2)
                    break
                elif category == 2:
                    time.sleep(1)
                    print("expenses chosen")
                    time.sleep(2)
                    break
                else:
                    print("Error: Please enter 1 or 2.")
                    time.sleep(2)
            except ValueError:
                print("Invalid input. Please enter a number (1 or 2).")
        description = input("Enter the details and reason: ")
        date = input("Enter the date: ")
        transaction = {
            "amount": amount,
            "category": category,
            "description": description,
            "date": date
        }

        transactions.append(transaction)

        choice = input("Add another transaction? (yes/no): ").strip().lower()
        time.sleep(2)
        if choice == "no":
            print("redirecting...")
            break

def view_summary():
       total_income = 0
       total_expense = 0
       for entry in transactions:
          if entry['category'] == 1 :
             total_income += entry['amount']
          elif entry['category'] == 2 :
             total_expense += entry['amount']
          else:
              print("error occured")

          balance = total_income -total_expense
          print("\n SUMMARY IS AS FOLLOWS: ----------------")
          print(f"total income: ₹{total_income}")
          print(f"total expense: ₹{total_expense}")
          print(f"Current balance: ₹{balance}")
          time.sleep(5)

def ai_use():
        from openai import OpenAI

        #IMPORTANT: API key should be set in environment as "my_api_python"
        # API key removed for security before uploading to GitHub

        client = OpenAI(base_url="https://api.groq.com/openai/v1", api_key=os.environ["my_api_python"])

        prompt="what are savings and how to manage money divided into income, rent, entertainment and expenses"
        response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
        {"role":"user","content":prompt}
         
            ]
               
        )
        print("Processing: ")
        print(response.choices[0].message.content)
        time.sleep(30)

def show_data():     #inside or outside the class?
        with open("list_record.txt","a") as f:
            for entry in transactions:
                line = f"{entry['amount']}|{entry['category']}|{entry['description']}|{entry['date']} \n\n"
                f.write(line)
        
        print("----- ALL TRANSACTIONS -----")
        try:
               with open("list_record.txt","r") as f:
                for line in f:
                    amount, category, description, date = line.strip().split("|")
                    print(f"₹{amount} ---is the amount")
                    print(f"{category} ------is the category")
                    print(f"{description} ----are the details")
                    print(f"{date} -----------is the date")
                    print("-------------------------------\n ")
                    #print(f" the current balance is : ₹{self.transaction} \n {self.category} \n {self.description} \n {self.date} ")
        except FileNotFoundError:
            print("no previous transaction file found. ")
            
        # if transactions:
        #  print("no transactions to display: ")
        #  return
        # for entry in transactions:
         

# class Finance_manager:
#     def __init__(self,transaction,category,description,date):
#         self.transaction=transaction
#         self.category=category
#         self.description=description
#         self.date=date
    

print("Hello user enter your credentials: ")
time.sleep(1)
while True:
 user_name=str(input("enter the username: "))
 password=str(input("enter the password: "))
 time.sleep(1)
 if user_name== "tejas" and password =="bansal" :
        time.sleep(1.5)
        print("logging you in...")
        time.sleep(1.5)
        print("authenticating...")
        time.sleep(1.5)
        print("creating a secure channel...")
        time.sleep(1.5)
        print("welcome user ")
        time.sleep(1.5)
        
        while True:
                show_menu()
                choice = input("enter your choice: ")

                if choice == '1' :
                    print("redirecting...")
                    time.sleep(1.5)
                    add_transaction()
                elif choice == '2' :
                    print("redirecting...")
                    time.sleep(1.5)
                    show_data()
                elif choice == '3':
                    print("redirecting...")
                    time.sleep(1.5)
                    view_summary()
                elif choice == '4':
                    print("redirecting...")
                    time.sleep(1.5)
                    ai_use()
                elif choice == '5':
                    print("Thank you for your time with us, bye for now! ")
                    print("logging you out...")
                    time.sleep(1.5)
                    break
                else:
                    print(" invalid input enter a number from 1,2,3,4,5")
                    print("redirecting...")
                    time.sleep(1.5)
 else :
        print("wrong username or password try again:")
        time.sleep(2)
    


    