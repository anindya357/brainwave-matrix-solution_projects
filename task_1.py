class User:
    user = []
    pin = []
    name = []
    balance = []

id_counter = 2000  # Global ID counter

obj = User()

def check_balance(lst,index):
    print(f"Your Account Balance is: {lst[index]}")

def withdraw(lst, index):
    amount = int(input("Enter Amount: "))
    if amount > lst[index]:
        print("You have insufficient balance.\n")
    else:
        lst[index] -= amount
        print("Withdrawal successful!\n")

def deposit(lst, index):
    deposit_money = int(input("Enter the amount to deposit: "))
    lst[index] += deposit_money
    print("Deposit successful!\n")

def transfer(lst, index):
    transfer_id = int(input("Enter Account No to Transfer: "))
    transfer_money = int(input("Enter Amount to Transfer: "))
    if transfer_money > lst[index]:
        print("You have insufficient balance.\n")
    else:
        found = False
        for i, user_id in enumerate(obj.user):
            if user_id == transfer_id:
                lst[i] += transfer_money
                lst[index] -= transfer_money
                print("Successfully Transferred!\n")
                found = True
                break
        if not found:
            print("Account not found!\n")



def show_account(nam, acc, bal, index):
   while True:
    print("Welcome to Your Account\n")
    print("- - - - - - \n")
    print(f"Name: {nam}")
    print(f"Account NO: {acc}")
    print("\nChoose an Option:")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Transfer")
    print("5. Logout")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        check_balance(obj.balance,index)
    elif choice == 2:
        withdraw(obj.balance, index)
    elif choice == 3:
        deposit(obj.balance, index)
    elif choice == 4:
        transfer(obj.balance, index)
    elif choice == 5:
        print("Logging Out...")
        break
    else:
        print("Invalid Option!")



def check_account():
    user_id = int(input("Enter your Account Number: "))
    user_pin = int(input("Enter your 4-digit pin: "))
    found = False
    for i in range(len(obj.user)):
        if obj.user[i] == user_id and obj.pin[i] == user_pin:
            show_account(obj.name[i], obj.user[i], obj.balance[i], i)
            found = True
            break
    if not found:
        print("Invalid Account No or Pin!\n")



def create_account():
    global id_counter
    Name = input("Enter Your Name: ")
    obj.name.append(Name)
    code = int(input("Enter your 4-digit pin: "))
    obj.pin.append(code)
    obj.user.append(id_counter)
    obj.balance.append(0)
    print("Account Created Successfully!\n")
    print(f"Your Account Number is: {id_counter} \n")
    print("Do Not Forget Your Pin Number\n")
    id_counter += 1  # Increment global ID counter for the next account


def main():
  while True :
    print("Welcome to ABC Bank Ltd\n")
    print("- - - - - - - \n")
    print("1. Log in")
    print("2. Create a New Account")
    print("3. Exit")
    option = int(input("Select an Option: "))

    if option == 1:
        check_account()
    elif option == 2:
        create_account()
    elif option ==3 :
         print("Exiting...")
         break
    else:
        print("Invalid Option!")


main()
