from entities.number import Number
import mysql.connector
from mysql.connector import Error
from entities.editt import Account
from helpers.operations import Operations
from helpers.connect import get_connection

OPS = Operations()

class Login:
    def __init__(self):
        pass

    @staticmethod
    def login_user() -> None:
        cardnum = input("Enter your 16-digit card number: ")

        try:
            cardnum = Number(cardnum).cardnum  # Use Number class for validation

            connection = get_connection()
            if connection and connection.is_connected():
                cursor = connection.cursor()

                select_query = """
                SELECT Name, Surname, balance, pin
                FROM people
                WHERE cardnum = %s
                """
                cursor.execute(select_query, (cardnum,))
                person = cursor.fetchone()

                if person:
                    stored_pin = person[3]
                    pin = input("Enter your PIN: ")

                    if pin == stored_pin:
                        print(f'''
Name: {person[0]}
Surname: {person[1]}
Balance: {person[2]}''')
                        Login.transaction_menu(person, cursor, connection, cardnum)
                    else:
                        print("Invalid PIN")
                else:
                    print("Card number not found")

        except ValueError as ve:
            print("Validation Error:", ve)
        except Error as e:
            print("Error while connecting to MySQL:", e)
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def transaction_menu(person, cursor, connection, cardnum):
        OPS.login_operations()
        choice = input("Enter your choice: ")

        if choice == "1":
            Login.cash_in(person, cursor, connection, cardnum)
        elif choice == "2":
            Login.withdraw(person, cursor, connection, cardnum)
        elif choice == "3":
            Login.transaction(person, cursor, connection, cardnum)
        elif choice == "4":
            Account.edit_pin(cursor, connection, cardnum) #abstraction inheritance
        else:
            print("Invalid choice")

    @staticmethod
    def cash_in(person, cursor, connection, cardnum):
        cash_in_amount = float(input("Enter the amount to cash in: "))
        if cash_in_amount > 0:
            update_query = """
            UPDATE people
            SET balance = balance + %s
            WHERE cardnum = %s
            """
            cursor.execute(update_query, (cash_in_amount, cardnum))
            connection.commit()
            print("Cash in successful!")
        else:
            print("Invalid amount. Amount should be greater than 0.")

    @staticmethod
    def withdraw(person, cursor, connection, cardnum):
        withdraw_amount = float(input("Enter the amount to withdraw: "))
        balance = float(person[2])  # Convert balance to float
        if withdraw_amount > 0:
            if withdraw_amount <= balance:
                update_query = """
                UPDATE people
                SET balance = balance - %s
                WHERE cardnum = %s
                """
                cursor.execute(update_query, (withdraw_amount, cardnum))
                connection.commit()
                print("Withdrawal successful!")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount. Amount should be greater than 0.")

    @staticmethod
    def transaction(person, cursor, connection, cardnum):
        receiver_cardnum = input("Enter the receiver's 16-digit card number: ")
        receiver_cardnum = Number(receiver_cardnum).cardnum  # Use Number class for validation
        select_receiver_query = """
        SELECT Name, Surname, balance
        FROM people
        WHERE cardnum = %s
        """
        cursor.execute(select_receiver_query, (receiver_cardnum,))
        receiver = cursor.fetchone()

        if receiver:
            transfer_amount = float(input("Enter the amount to transfer: "))
            if transfer_amount > 0:
                balance = float(person[2])  # Convert balance to float
                if transfer_amount <= balance:
                    update_sender_query = """
                    UPDATE people
                    SET balance = balance - %s
                    WHERE cardnum = %s
                    """
                    cursor.execute(update_sender_query, (transfer_amount, cardnum))

                    update_receiver_query = """
                    UPDATE people
                    SET balance = balance + %s
                    WHERE cardnum = %s
                    """
                    cursor.execute(update_receiver_query, (transfer_amount, receiver_cardnum))

                    connection.commit()
                    print("Transaction successful!")
                else:
                    print("Insufficient balance.")
            else:
                print("Invalid amount. Amount should be greater than 0.")
        else:
            print("Receiver's card number not found.")

# Example usage
# if __name__ == "__main__":
#     login_instance = Login()
#     login_instance.login_user()
