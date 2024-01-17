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
