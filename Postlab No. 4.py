print('Welcome to Philippine National Bank')
restart = ('Y')
chances = 3
balance = 100

while chances >=0:
    pin = int(input("Please enter 6 digit pin: "))
    if pin == (123456):
        print("You entered correctly!\n")
        while restart not in('n', 'No', 'no', 'N'):
            print("Please press 1 for your Balance \n")
            print("Please press 2 to make a withdraw \n")
            print("Please press 3 to deposit \n")
            print("Please press 4 to return card \n")
            option = int(input("What would you like to choose?: "))
            if option == 1:
                print("Your Balance is: ", balance, '\n')
                restart = input("Would you like to go back?")
                if restart in ('n', 'No', 'no', 'N'):
                    print("Thank You!")
                    break
            elif option == 2:
                option2 = ('y')
                withdrawal1 = float(input("How much would you like to withdraw? \n10/20/40/60/80/100 for other enter 1: "))
                if withdrawal1 in [10,20,30,40,50,60,70,80,90,100]:
                    balance = balance - withdrawal1
                    print("Thank You!")
                    break
                elif withdrawal1 != [10,20,30,40,50,60,70,80,90,100]:
                    print("Invalid Amount, Please Try Again\n")
                    restart = ('y')
                elif withdrawal1 == 1:
                    withdrawal1 = float(input("Please Enter Desired Amount: "))
            elif option == 3:
                deposit = float(input("How much would you like to deposit?: "))
                balance = balance + deposit
                print("\nYour Balance is now: ", balance)
                restart = input("Would you like to to go back?: ")
                if restart in ('n', 'No', 'no', 'N'):
                    print("Thank You!")
                    break
            elif option == 4:
                print("Please wait while you card is Returned....\n")
                print("Thank You for using!")
                break
            else:
                print("Please Enter correct amount.:  \n")
                restart = ('y')
    elif pin != ('123456'):
        print("Incorrect pin")
        chances = chances - 1
        if chances == 0:
            print("\nNo more tries. Calling for the police.")
            break

def verifyPin(pin):
    if pin == '123456':
        return True
    else:
        return False
def log_in():
    tries = 0
    while tries < 4:
        pin = input("Please enter your 6 digit pin: ")
        if verifyPin(pin):
            print("Pin Accepted")
            return True
        else:
            print("Invalid pin")
            tries +=1
    print("Too man incorrect tries, Could not Log in")
    return False