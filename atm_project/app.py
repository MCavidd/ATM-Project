from entities.person import Person
from entities.login import Login
from entities.number import Number 
from entities.search import Search
from helpers.operations import Operations
from entities.filter import Filter


if __name__ == "__main__":
    PER = Person()
    LOG = Login()
    SRC = Search()
    OPS = Operations()
    FLTR = Filter()
    while True:
        ans = OPS.main_operations()
        if ans == "1":
            def get_valid_input(prompt):
                while True:
                    value = input(prompt)
                    if value.isalpha():
                        return value
                    else:
                        print("Invalid input. Please enter only letters.")
            name = get_valid_input("Enter name: ")
            surname = get_valid_input("Enter surname: ")
            print(f"Name: {name}")
            print(f"Surname: {surname}")
            cardnum = input("Enter card number: ")
            while not cardnum.isdigit() or len(cardnum) != 16:
                print("Card number must be a 16-digit number")
                cardnum = input("Enter card number: ")
            pin = input("Enter PIN: ")
            while not pin.isdigit() or len(pin) != 4:
                print("PIN must be a 4-digit number")
                pin = input("Enter pin: ")
            balance = 0   
            PER.add_to_db(name,surname,cardnum,pin,balance)
        if ans == "2":
            PER.delete_person()
        if ans == "3":
            LOG.login_user() 
        if ans =="4":
            name = input("Enter name: ")
            SRC.filter_by_name(name)
        if ans == "5":
            SRC.show_deleted_persons()
        if ans == "6":
            FLTR.filter_by_balance()
        if ans == "exit":
            print("GOODBYE :) ")
            break             
                 
            
                

        
       
        
