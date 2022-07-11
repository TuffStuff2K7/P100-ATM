class ATM:
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
        print("New balance:", self.balance)

    def withdrawal(self, amount):
        self.balance -= amount
        print("New balance:", self.balance)
    
    def enquiry(self):
        print("Your balance is:", self.balance)

def main():
    cardNumber = input("Enter card number: ") 
    pinNumber = input("Enter PIN number: ")
    cardHolder = ATM(cardNumber, pinNumber)

    print("(1) Deposit")
    print("(2) Withdraw")
    print("(3) Balance enquiry")
    i = int(input("Choose operation: "))

    if i == 1:
        amount = int(input("Enter amount for deposit: "))
        cardHolder.deposit(amount)
    elif i == 2:
        amount = int(input("Enter amount for withdrawal: "))
        cardHolder.withdrawal(amount) 
    else:
        cardHolder.enquiry()        

if __name__ == "__main__":
    main()