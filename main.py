"""
class ATM:
    def __init__(self):
        self.Amount_of_money = 100000


class User:
    def __init__(self):
        self.Account_Number = 0
        self.password = 0
        self.balance = 0


def Exist_acc(acc_num):
    with open("Record.txt", "r") as check:
        for line in check:
            u = User()
            values = line.split()
            u.Account_Number = int(values[0])
            if u.Account_Number == acc_num:
                return True
    return False


def valid_pass(passw):
    return passw <= 9999


def write_record():
    with open("Record.txt", "a") as in_file:
        A = ATM()
        U = User()
        U.Account_Number = int(input("Enter your Account Number: "))
        if Exist_acc(U.Account_Number):
            print("Account number already exists")
            return
        else:
            U.password = int(input("Enter your Password: "))
            if valid_pass(U.password):
                in_file.write(f"{U.Account_Number} {U.password} {U.balance}\n")
                print("Added Successfully")
            else:
                print("Invalid")


def read_user():
    with open("Record.txt", "r") as record:
        print("Acc_Number\tbalance")
        for line in record:
            acc_num, balance = line.split()
            print(f"{acc_num}\t\t{balance}")




def Search_By_Card_Number():
    str = int(input("Enter the Account_Number to search for: "))
    password = int(input("Please Enter Your password: "))

    found = False

    A = ATM()
    U = User()
    with open("Record.txt", "r") as in_file:
        for line in in_file:
            values = line.split()
            U.Account_Number = int(values[0])
            U.password = int(values[1])
            U.balance = float(values[2])
            if str == U.Account_Number:
                if U.password == password:
                    print()
                    print("Your Account_Number is", U.Account_Number)
                    print("Your Curr_Balance is", U.balance)
                    found = True
                    break
                else:
                    print("Please Enter a Valid Password")
    if not found:
        print("Record not found")


def Update_record():
    with open("Record.txt", "r+") as record:
        A = ATM()
        U = User()
        ch = 'y'
        operation = 0
        money = 0.0
        acc_num = int(input("Enter Your Account Number: "))
        if not Exist_acc(acc_num):
            print("Account not found")
            return
        else:
            passw = int(input("Enter Your Password: "))
            found = False
            lines = record.readlines()
            record.seek(0)
            for line in lines:
                values = line.split()
                U.Account_Number = int(values[0])
                U.password = int(values[1])
                U.balance = float(values[2])
                if U.Account_Number == acc_num and U.password == passw:
                    found = True
                    while ch == 'y':
                        print("1: To deposit")
                        print("2: To withdraw")
                        operation = int(input("Enter the operation: "))
                        if operation == 1:
                            money = float(input("Enter the value: "))
                            U.balance += money
                            A.Amount_of_money += money
                            record.write(f"{U.Account_Number} {U.password} {U.balance}\n")
                            print("Added successfully")
                        elif operation == 2:
                            money = float(input("Enter the withdrawal amount: "))
                            if money > A.Amount_of_money or money > U.balance:
                                print("Invalid")
                            else:
                                U.balance -= money
                                A.Amount_of_money -= money
                                record.write(f"{U.Account_Number} {U.password} {U.balance}\n")
                                print("Withdrawal successful")
                        ch = input("Do you want to make operation again(y/n): ")
                    break
        if not found:
            print("Invalid account number and password")


def main():
    x = int(input("1 - To add user\n2 - To read all users\n3 - To search by card number\n4 - To make(deposit/withdraw)\n"))
    if x == 1:
        write_record()
    elif x == 2:
        read_user()
    elif x == 3:
        Search_By_Card_Number()
    elif x == 4:
        Update_record()


main()
"""


def WriteRecord():
    with open('ATM_User_Records.txt', 'a') as file:
        c = 'y'
        while c == 'y':
            Acc_Num = input('Enter Your Account Number : ')
            Password = int(input('Enter Your Password : '))
            Balance = int(input('Enter Your Balance : '))
            if Password < 9999:
                if Balance <= 100000:
                    file.write(str(Acc_Num) + '\t\t' +
                               str(Password) + '\t\t' + str(Balance) + '\n')
                else:
                    print('Budget exceeded')
            else:
                print('Password Must be 4 Numbers OR Less!!')
            c = input('Do you want to Enter Another Account? (y / n): ')
        print('Operation Completed Successfully!')


def ReadRecord():
    with open('ATM_User_Records.txt', 'r') as file:
        print('Account Number\tPassword\tBalance')
        for line in file:
            print(line, end='')


def SearchRecord():
    Acc_Num = input('Enter Your Account Number: ')
    with open('ATM_User_Records.txt', 'r') as file:
        flag = False
        for line in file:
            fields = line.split('\t')
            if fields[0] == Acc_Num:
                flag = True
                print('Account Number\tPassword\tBalance')
                print(line, end='')
        if not flag:
            print('Account Not Found!')


def DeleteRecord():
    import os
    Acc_Num = input('Enter Account You want to Delete: ')
    file = open('ATM_User_Records.txt', 'r')
    tempfile = open('Temp_ATM_User_Records.txt', 'w')
    flag = False
    for line in file:
        fields = line.split('\t')
        if fields[0] == Acc_Num:
            flag = True
        else:
            tempfile.write(line)
    file.close()
    tempfile.close()
    os.remove('ATM_User_Records.txt')
    os.rename('Temp_ATM_User_Records.txt', 'ATM_User_Records.txt')
    if not flag:
        print('Account Not Found!')
    else:
        print('Account Deleted Successfully!')


def UpdateRecord():
    import os
    Acc_num = input('Enter your Account Number: ')
    password = input('Enter your Password: ')
    flag = False
    file = open('ATM_User_Records.txt', 'r')
    tempfile = open('Temp_ATM_User_Records.txt', 'w')
    for line in file:
        st = line.split('\t\t')
        if Acc_num == st[0]:
            if password == st[1]:
                flag = True
                balance = int(st[2])
                operation = input('the operation (1: deposit, 2: withdraw): ')
                if operation == "1":
                    amount = int(input('Enter the deposit amount: '))
                    balance += amount
                    if balance <= 100000:
                        line = str(Acc_num) + '\t\t' + \
                            str(password) + '\t\t' + str(balance) + '\n'
                    else:
                        print("Budget exceeded please don't exceed 100000")
                elif operation == "2":
                    amount = int(input('Enter the withdrawal amount: '))
                    if amount <= balance:
                        balance -= amount
                        line = str(Acc_num) + '\t\t' + \
                            str(password) + '\t\t' + str(balance) + '\n'
                    else:
                        print("Insufficient balance")
        tempfile.write(line)
    file.close()
    tempfile.close()
    os.remove('ATM_User_Records.txt')
    os.rename('Temp_ATM_User_Records.txt', 'ATM_User_Records.txt')
    if flag:
        print('thank you')
    else:
        print('you entered Invalid Account_Number or Password')


def Home():
    c = 'y'
    while c == 'y':
        print('1: To add new Account.')
        print('2: To read all Accounts.')
        print('3: To search for Account.')
        print('4: To update an Account.')
        print('5: To delete an Account.')
        c = input('Your Choice: ')
        if c == '1':
            WriteRecord()
        if c == '2':
            ReadRecord()
        if c == '3':
            SearchRecord()
        if c == '4':
            UpdateRecord()
        if c == '5':
            DeleteRecord()
        c = input('Perform another operation (y / n): ')


Home()
