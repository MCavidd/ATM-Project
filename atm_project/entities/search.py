import mysql.connector
from mysql.connector import Error
from helpers.connect import get_connection

class Search:
    @staticmethod
    def filter_by_name(name: str) -> None:
        try:
            connection = get_connection()
            if connection and connection.is_connected():
                cursor = connection.cursor(dictionary=True)

                # Query to find all records with the given name
                search_query = """
                SELECT Name, Surname, cardnum, pin, balance
                FROM people
                WHERE Name = %s
                """
                cursor.execute(search_query, (name,))
                results = cursor.fetchall()

                if results:
                    for row in results:
                        print(f'''
Name: {row['Name']}
Surname: {row['Surname']}
Card Number: {row['cardnum']}
PIN: {row['pin']}
Balance: {row['balance']}
======================================''')
                else:
                    print("No records found for the given name.")

        except Error as e:
            print("Error while connecting to MySQL:", e)
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

    @staticmethod
    def show_deleted_persons() -> None:
        try:
            connection = get_connection()
            if connection and connection.is_connected():
                cursor = connection.cursor(dictionary=True)

                option = input('''
1---> Show deleted persons
2---> Return person to the database: ''')

                if option == '1':
                    # Query to find all deleted persons in delete2 table
                    deleted_query = """
                    SELECT id, name, surname, cardnum, pin, balance
                    FROM delete2
                    """
                    cursor.execute(deleted_query)
                    results = cursor.fetchall()

                    if results:
                        for row in results:
                            print(f'''
================= {row['id']} ================
Name: {row['name']}
Surname: {row['surname']}
Card Number: {row['cardnum']}
Balance: {row['balance']}
=============================================''')
                    else:
                        print("No deleted records found.")

                elif option == '2':
                    # Prompt the user for the details of the person to be returned
                    name = input("Enter the Name: ")
                    surname = input("Enter the Surname: ")
                    cardnum = input("Enter the Card Number: ")

                    # Start a transaction
                    connection.start_transaction()

                    try:
                        # Query to return the specified person to the people table
                        return_query = """
                        INSERT INTO people (Name, Surname, cardnum, pin, balance)
                        SELECT name, surname, cardnum, pin, balance
                        FROM delete2
                        WHERE name = %s AND surname = %s AND cardnum = %s
                        """
                        cursor.execute(return_query, (name, surname, cardnum))

                        # Check if the person was actually returned
                        if cursor.rowcount == 0:
                            print("No matching deleted person found.")
                        else:
                            # Query to delete the specified record from delete2 table
                            delete_query = """
                            DELETE FROM delete2
                            WHERE name = %s AND surname = %s AND cardnum = %s
                            """
                            cursor.execute(delete_query, (name, surname, cardnum))

                            # Commit the transaction
                            connection.commit()

                            print("The specified person has been returned to the people table.")

                    except Error as e:
                        # Rollback the transaction in case of error
                        connection.rollback()
                        print("Error during the transaction:", e)

                else:
                    print("Invalid option selected.")

        except Error as e:
            print("Error while connecting to MySQL:", e)
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

