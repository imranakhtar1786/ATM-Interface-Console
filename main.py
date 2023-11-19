import re
import sys
from dao import *
from bean import Bean
log=Login()
bean=Bean()
def welcome():
    try:
        print("Welcome " + bean.getname())
        while(True):
            print("1.Cash Withdraw")
            print("2.Deposit Cash")
            print("3.Transfer Amount")
            print("4.Transaction History")
            print("5.Quit")
            a = input("Enter:")
            match a:
                case '1':
                    bean.setTransType("Withdraw")
                    bean.setDebitAmmount(float(input("Enter Amount:")))
                    b = Withdrow()
                    b = b.withdrow(bean)
                    if (b == 1):
                        print("Withdraw Successful")
                        login()
                        break
                    else:
                        print("Withdraw Failed")
                        login()
                        break
                case '2':
                    bean.setTransType("Deposit")
                    bean.setCreditAmmount(float(input("Enter Amount:")))
                    b = Deposit()
                    b = b.deposit(bean)
                    if (b == 1):
                        print("Deposit Successful ")
                        login()
                        break
                    else:
                        print("Deposit Failed")
                        login()
                        break
                case '3':
                    bean.setTransType("Transfer")
                    bean.setTransferAmmount(float(input("Enter Amount:")))
                    b = input("Enter Account No:")
                    if (len(b) == 10):
                        bean.setAccountNo1(b)
                        c = Transfer()
                        c = c.transfer(bean)
                        if (c == 1):
                            print("Transfer Successful")
                            login()
                            break
                        else:
                            print("Transfer Failed")
                            login()
                            break
                    else:
                        print("Enter Valid Account No.")
                case '4':
                    b = input("Enter Date(yyyy-mm-dd):")
                    if (re.compile(r'^\d{4}-\d{2}-\d{2}$').match(b)):
                        d = TransactionHistory()
                        c = d.Transaction(bean, b)
                        for i in c:
                            print(*i, sep="   ")
                    else:
                        print("Enter Valid Date")
                case '5':
                    login()
                    break
                case _:
                    print("Existing......")
    except KeyboardInterrupt:
        sys.exit(0)
def login():
    try:
        a = input("Enter ID:")
        a1 = input("Enter PIN:")
        if (len(a) < 5 or len(a1) != 4 or a1.isnumeric() == 0):
            print("Enter valid ID and PIN")
            login()
        else:
            c = log.login(a, int(a1), bean)
            if (c == 1):
                welcome()
            else:
                print("Invalid Id and PIN")
                login()
    except KeyboardInterrupt:
        sys.exit(0)
login()


