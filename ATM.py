import time


class ATM:

    def ben(self):
        f = open("db.txt","r+")
        data = float(f.read())
        print('Your Account Balance is: ', data)
        f.close()
        print('\n\nRedirecting to main menu')
        time.sleep(5)
        self.menu()

    def wdr(self):
        f = open("db.txt", "r+")
        data = float(f.read())
        data = float(data)
        withdraw = int(input('Enter the amount you want to withdraw: '))
        if withdraw <= data:
            data -= withdraw
            data = str(data)
            f.seek(0)
            f.write(data)
            choice = input('Press Y/y, if you want to check your remaining balance. Otherwise type anything else')
            if choice == 'Y' or choice == 'y':
                print('Your Account Balance is: ', data)
        else:
            print('You Have insufficient Balance , Enter Amount less than',data)
        f.close()
        print('\n\nRedirecting to main menu')
        time.sleep(3)
        self.menu()

    def add(self):
        f = open("db.txt","r+")
        data = float(f.read())
        amount = float(input('Enter the amount you want to add: '))
        data += amount
        data = str(data)
        f.seek(0)
        f.write(data)
        choice = input('Press Y/y, if you want to check your remaining balance. Otherwise type anything else')
        if choice == 'Y' or choice == 'y':
            print('Your Account Balance is: ',data)
        f.close()
        print('\n\nRedirecting to main menu')
        self.menu()

    def menu(self):
        print('  \n1.Balance Enquiry  \n2.Withdrawal  \n3.ADD Amount  \n4.Exit')
        ch = input('Enter Choice: ')
        if ch == '1':
            self.ben()
        elif ch == '2':
            self.wdr()
        elif ch == '3':
            self.add()
        elif ch == '4':
            exit()
        else:
            print('Please Enter Correct Choice: ')

print('Insert your card')
time.sleep(4)
print('Card read Successfully')
pin = input('Enter PIN: ')
atm = ATM()
atm.menu()
